# --coding:utf-8--
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Candlestick, Bar, Grid, Line
from utils.paths import HOME


def backtest_plot(kline_df, module_results, module_alarms):
    n_modules = len(module_results)
    candle_percent = int(90 / (n_modules + 1)) + 10
    module_percent = int(90 / (n_modules + 1))
    top = 1
    date_tickers = kline_df["datetime"].to_list()
    kline_data = list(
        zip(
            kline_df["open"].tolist(),
            kline_df["close"].tolist(),
            kline_df["low"].tolist(),
            kline_df["high"].tolist(),
        ),
    )

    grid_chart = Grid(
        init_opts=opts.InitOpts(
            width="90%",
            height="95vh",
            page_title="画图工具",
            animation_opts=opts.AnimationOpts(animation=False),
        )
    )

    kline = (
        Candlestick()
            .add_xaxis(date_tickers)
            .add_yaxis(
            series_name="",
            y_axis=kline_data,
            itemstyle_opts=opts.ItemStyleOpts(
                color="red", color0="green", border_color="red", border_color0="green"
            ),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="", pos_left="0"),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                is_scale=True,
                boundary_gap=False,
                axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
                split_number=20,
                min_="dataMin",
                max_="dataMax",
                name_textstyle_opts=opts.TextStyleOpts(font_size=8),
            ),
            yaxis_opts=opts.AxisOpts(
                is_scale=True,
                splitline_opts=opts.SplitLineOpts(is_show=True),
                name_textstyle_opts=opts.TextStyleOpts(font_size=8),
            ),
            tooltip_opts=opts.TooltipOpts(
                trigger="axis",
                axis_pointer_type="line",
                position=["100%", "1%"],
                textstyle_opts=opts.TextStyleOpts(font_size=8),
            ),
            datazoom_opts=[
                opts.DataZoomOpts(
                    is_show=False,
                    type_="inside",
                    xaxis_index=list(range(len(module_results) + 1)),
                    range_start=0,
                    range_end=5,
                ),
            ],
        )
    )
    grid_chart.add(
        kline,
        grid_opts=opts.GridOpts(
            pos_left="3%",
            pos_right="1%",
            pos_top=f"{top}%",
            height=f"{candle_percent-3}%",
        ),
    )
    top += candle_percent
    for module_name, module_points in module_results.items():
        tmp_df = pd.DataFrame(module_points)
        tmp_df.to_csv("test.csv")
        line = Line().add_xaxis(tmp_df["datetime"].tolist())
        for c in tmp_df.columns:
            if c != "datetime":
                line.add_yaxis(series_name=c,
                               y_axis=tmp_df[c].tolist(),
                               is_smooth=True,
                               is_hover_animation=False,
                               label_opts=opts.LabelOpts(is_show=False), )
        line.set_global_opts(
            title_opts=opts.TitleOpts(title="", pos_left="0"),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                is_scale=True,
                boundary_gap=False,
                axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
                split_number=20,
                min_="dataMin",
                max_="dataMax",
                name_textstyle_opts=opts.TextStyleOpts(font_size=8),
            ),
            yaxis_opts=opts.AxisOpts(
                is_scale=True,
                splitline_opts=opts.SplitLineOpts(is_show=True),
                name_textstyle_opts=opts.TextStyleOpts(font_size=8),
            ),
            tooltip_opts=opts.TooltipOpts(
                trigger="axis",
                axis_pointer_type="line",
                position=["100%", "1%"],
                textstyle_opts=opts.TextStyleOpts(font_size=8),
            ),
            datazoom_opts=[
                opts.DataZoomOpts(
                    is_show=False,
                    type_="inside",
                    xaxis_index=list(range(len(module_results) + 1)),
                    range_start=0,
                    range_end=5,
                ),
            ],
        )
        grid_chart.add(line,
                       grid_opts=opts.GridOpts(
                           pos_left="3%",
                           pos_right="1%",
                           pos_top=f"{top}%",
                           height=f"{module_percent-3}%",
                       ))
        top += module_percent

    path = HOME.joinpath("__result.html")
    grid_chart.render(str(path))
    return str(path)
