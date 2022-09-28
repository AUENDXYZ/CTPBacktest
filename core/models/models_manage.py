# --coding:utf-8--
from typing import Dict, List
from core.metrics.modules_manage import SingleModule


class ModelManager:
    def __init__(self):
        self.models: Dict[str, 'SingleModel'] = {}

    def load_models(self):
        pass

    def save_model(self, model):
        pass



    def add_model(self, model: 'SingleModel'):
        if model.name in self.model_names:
            raise ValueError("名称已存在")
        self.models[model.name] = model

    @property
    def model_names(self):
        return list(self.models.keys())


class SingleModel:
    def __init__(self, name: str, kline_interval: int, direction: str,  modules: List):
        self.name = name
        self.kline_interval = kline_interval
        self.direction = direction
        self.modules = modules

    def describe(self):
        tooltips = "\n".join(["【" + m.name + "】" + m.tooltip() for m in self.modules])
        return (f"名称: {self.name}\n"
                f"k线周期: {self.kline_interval} 分钟\n"
                f"方向: {self.direction}\n"
                "---\n"
                "指标:\n"
                f"{tooltips}\n"
                "---")

    def update_value(self):
        # 更新module
        pass
