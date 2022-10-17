# --coding:utf-8--
import os
import json
import datetime as dt
import pandas as pd
from functools import lru_cache
from pathlib import Path
from hashlib import md5
from operator import gt, lt, eq, ne
from collections import defaultdict
from utils.paths import MODULE_MAPPING_NAME





def get_python_files(file_path: Path):
    files = [
        f
        for f in os.listdir(file_path)
        if (f.endswith(".py")) and ("__init__" not in f)
    ]
    # 文件名:文件路径
    return {i[:-3]: file_path.joinpath(i) for i in files}


@lru_cache()
def gen_fake_values(interval=1, length=200):
    # 生成一段假数据用于初步测试
    start = dt.datetime(2022, 9, 19, 9, 0, 0)
    datetime, open, close, high, low, volume = [], [], [], [], [], []
    for i in range(0, length * interval, interval):
        datetime.append(start + dt.timedelta(minutes=i))
        open.append(i)
        close.append(i)
        high.append(i)
        low.append(i)
        volume.append(i)
    res = {
        "datetime": datetime,
        "open": open,
        "close": close,
        "high": high,
        "low": low,
        "volume": volume,
    }
    df = pd.DataFrame(res)
    df.set_index("datetime", inplace=True)
    res["df"] = df
    return res


def get_module_mapping_name(module_name: str):
    # 自定义添加的module文件命名是一段MD5, 映射关系保存在 MODULE_MAPPING_NAME 文件中
    # 在可以命名的情况下module_name是可以直接作为md5_name使用的
    if not MODULE_MAPPING_NAME.exists():
        return module_name
    mappings = json.loads(MODULE_MAPPING_NAME.read_text(encoding="utf-8"))
    if module_name not in mappings:
        return module_name
    return mappings[module_name]


def get_module_module_name(md5_name: str):
    if not MODULE_MAPPING_NAME.exists():
        return md5_name
    mappings: dict = json.loads(MODULE_MAPPING_NAME.read_text(encoding="utf-8"))
    mappings_reverse = {v: k for k, v in mappings.items()}
    if md5_name not in mappings_reverse:
        return md5_name
    return mappings_reverse[md5_name]


def set_module_mapping_name(module_name: str):
    if not MODULE_MAPPING_NAME.exists():
        mappings = {}
    else:
        mappings = json.loads(MODULE_MAPPING_NAME.read_text(encoding="utf-8"))
    md5_name = md5(module_name.encode("utf-8")).digest()
    mappings[module_name] = md5_name
    with open(MODULE_MAPPING_NAME, "w", encoding="utf-8") as f:
        json.dump(f, mappings, ensure_ascii=False, indent=4)
    return md5_name


def remove_module_mapping_name(module_name: str):
    if not MODULE_MAPPING_NAME.exists():
        return
    mappings = json.loads(MODULE_MAPPING_NAME.read_text(encoding="utf-8"))
    if module_name in mappings:
        mappings.pop(module_name)
    with open(MODULE_MAPPING_NAME, "w", encoding="utf-8") as f:
        json.dump(f, mappings, ensure_ascii=False, indent=4)


__mapping = {">": gt, "<": lt, "=": eq, "!=": ne}


def compare_type(symbol):
    return __mapping[symbol]


def load_data(file_path):
    df = pd.read_csv(file_path, encoding="gbk", encoding_errors="ignore")
    return df


def is_weekday(date: dt.date):
    return date.weekday() + 1 < 6


time_59_59 = dt.time(23, 59)
time_0_0 = dt.time(0, 0)


@lru_cache()
def is_in_time_range(target: dt.time, left: dt.time, right: dt.time):
    if left <= right:
        return left <= target <= right
    else:
        return left <= target <= time_59_59 or time_0_0 <= target <= right


def trade_time_dict(trade_range_array):
    _dict = defaultdict(bool)
    for i in range(1440):
        t = dt.time(hour=i // 60, minute=i % 60)
        for [left, right] in trade_range_array:
            if is_in_time_range(t, left, right):
                _dict[t] = True
                break
    return _dict
