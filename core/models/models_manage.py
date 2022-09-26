# --coding:utf-8--
from typing import Dict, List
from core.metrics.modules_manage import SingleModule


class ModelManage:
    def __init__(self):
        self.models: Dict[str, 'SingleModel'] = {}


class SingleModel:
    def __init__(self, name: str, kline_interval: int, modules: List['SingleModule']):
        self.name = name
        self.kline_interval = kline_interval
        self.modules = modules

    def update_value(self):
        # 更新module
        pass



