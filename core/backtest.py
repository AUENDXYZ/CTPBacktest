# --coding:utf-8--
import pandas as pd
import numpy as np
import datetime as dt
from PySide6.QtCore import Signal
from .models.models_manage import SingleModel
from utils.tools import trade_time_dict
from utils.plot import backtest_plot


def run_backtest(
    df: pd.DataFrame,
    model: SingleModel,
    trade_range,
    column_alias,
    progress_callback: Signal,
    alarm_callback: Signal,
):
    alarm_callback.emit("##########")
    alarm_callback.emit("开始回测")
    alarm_callback.emit("策略详情:\n" + model.describe())
    alarm_callback.emit(
        "交易时间:\n" + "\n".join([f"{str(i[0])}-{str(i[1])}" for i in trade_range])
    )
    time_dict = trade_time_dict(trade_range)

    alarm_callback.emit(f"tick数据长度: {len(df)}")
    df = df[list(column_alias.values())]
    df = df.rename(columns={v: k for k, v in column_alias.items()})
    df = df.astype(np.float32, errors="ignore")
    df["datetime"] = pd.to_datetime(df["datetime"])
    alarm_callback.emit("正在预处理数据")
    kline_generator = KLineGenerator(df, model.kline_interval, time_dict)
    alarm_callback.emit("正在回测")
    kline_df = pd.DataFrame(
        columns=["datetime", "open", "close", "high", "low", "volume"]
    )
    kline_df.set_index("datetime")

    datetime_que = []
    open_que = []
    close_que = []
    high_que = []
    low_que = []
    volume_que = []
    module_results = {module.name: [] for module in model.modules}
    modulr_alarms = {module.name: [] for module in model.modules}
    for k in kline_generator.kline_stream():
        datetime_que.append(k["datetime"])
        close_que.append(k["close"])
        open_que.append(k["open"])
        high_que.append(k["high"])
        low_que.append(k["low"])
        volume_que.append(k["volume"])
        kline_df.loc[k["datetime"]] = k

        for module in model.modules:
            module.update_value(
                datetime=datetime_que[-200:],
                open=open_que[-200:],
                close=close_que[-200:],
                high=high_que[-200:],
                low=low_que[-200:],
                volume=volume_que[-200:],
                df=kline_df[-200:],
            )
            module.backtest()
            module_results[module.name].append(module.result)
            if module.catch_condition():
                modulr_alarms[module.name].append(datetime_que[-1])
    alarm_callback.emit("开始画图")
    file_path = backtest_plot(kline_df, module_results, modulr_alarms)
    alarm_callback.emit("回测结束")
    alarm_callback.emit("##########")
    return file_path


class KLineGenerator:
    def __init__(self, df: pd.DataFrame, kline_interval: int, time_points: dict):
        self.df = df
        self.kline_interval = kline_interval
        self.time_points = time_points
        self.kline_1min = pd.DataFrame(
            columns=["datetime", "open", "close", "high", "low", "volume"]
        )
        self.to_1min()

    def to_1min(self):
        """先将数据转化为1分钟k线"""
        curr_minute = None
        curr_point = {}

        def update_point():
            if "datetime" not in curr_point:
                curr_point["datetime"] = curr_minute
            if "open" not in curr_point:
                curr_point["open"] = row.price
            curr_point["close"] = row.price
            if "high" in curr_point:
                curr_point["high"] = max(row.price, curr_point["high"])
            else:
                curr_point["high"] = row.price
            if "low" in curr_point:
                curr_point["low"] = min(row.price, curr_point["low"])
            else:
                curr_point["low"] = row.price
            if "volume" in curr_point:
                curr_point["volume"] += row.volume
            else:
                curr_point["volume"] = row.volume

        def save_point():
            self.kline_1min.loc[len(self.kline_1min)] = curr_point
            curr_point.clear()

        for index, row in self.df.iterrows():
            if curr_minute is None:
                curr_minute = row.datetime.replace(
                    second=0, microsecond=0
                ) + pd.Timedelta(minutes=1)
            elif curr_minute < row.datetime:
                save_point()
                curr_minute = row.datetime.replace(
                    second=0, microsecond=0
                ) + pd.Timedelta(minutes=1)
            update_point()

    def kline_stream(self):
        count = 0
        point = {}
        for index, row in self.kline_1min.iterrows():
            if not self.time_points[row.datetime.time()]:
                continue
            if row.datetime.minute == 0 and row.datetime.hour == 9:
                # 9点作为新的开始
                count = 0
                point.clear()
            if not point:
                point["datetime"] = row.datetime
                point["open"] = row.open
                point["close"] = row.close
                point["high"] = row.high
                point["low"] = row.low
                point["volume"] = row.volume
            else:
                point["datetime"] = row.datetime
                point["close"] = row.close
                point["high"] = max(point["high"], row.high)
                point["low"] = min(point["low"], row.low)
                point["volume"] += row.volume
            count += 1
            between = int((row.datetime - point["datetime"]).total_seconds() // 60)
            if between != 1:
                for i in range(1, between):
                    if self.time_points[
                        (point["datetime"] + pd.Timedelta(minutes=i)).time()
                    ]:
                        count += 1

            if count >= self.kline_interval:
                yield point
                count = 0
                point.clear()
