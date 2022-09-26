# coding:utf-8
try:
    import ujson as json
except ImportError:
    import json
from utils.paths import SETTING_JSON

Setting = {}


def read_setting():
    with open(str(SETTING_JSON), "r", encoding="utf-8") as f:
        _json = json.load(f)
    for k, v in _json.items():
        Setting[k] = v


def write_setting(key, value):
    Setting[key] = value
    with open(str(SETTING_JSON), "w", encoding="utf-8") as f:
        json.dump(Setting, f, ensure_ascii=False, indent=4)


read_setting()
