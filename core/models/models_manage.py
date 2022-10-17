# --coding:utf-8--
try:
    import pandas._libs.json as json
except ImportError:
    import json
from typing import Dict, List
from functools import partial
from core.metrics.modules_manage import SingleModule
from database.sqlite import Models
from utils.tools import compare_type


class ModelManager:
    def __init__(self, module_manager):
        self.module_manager = module_manager
        self.models: Dict[str, "SingleModel"] = {}
        self.load_models()

    def load_models(self):
        for db_model in Models.select():
            modules = json.loads(db_model.modules)
            modules_list = []
            for module_params in modules:
                module = self.module_manager.modules[module_params["module_name"]](
                    module_params["serial_name"]
                )
                module.set_metric_params(**module_params["metric_params"])
                module.set_condition(
                    **{
                        k: lambda x: compare_type(v[1])(x, float(v[2]))
                        for k, v in module_params["condition_tip"].items()
                    }
                )
                module.set_condition_tip(**module_params["condition_tip"])
                modules_list.append(module)

            self.models[db_model.name] = SingleModel(
                db_model.name, db_model.kline_interval, db_model.direction, modules_list
            )

    def save_model(self):
        for model_name, single_model in self.models.items():
            kline_interval = single_model.kline_interval
            direction = single_model.direction
            modules = []
            for module in single_model.modules:
                modules.append(
                    {
                        "module_name": module.name,
                        "serial_name": module.serial_name,
                        "metric_params": module.metric_params,
                        "condition_tip": module.condition_tip,
                    }
                )
            Models.get_or_create(
                name=model_name,
                defaults=dict(
                    kline_interval=kline_interval,
                    direction=direction,
                    modules=json.dumps(modules),
                ),
            )

    def add_model(self, model: "SingleModel"):
        if model.name in self.model_names:
            raise ValueError("名称已存在")
        self.models[model.name] = model
        self.save_model()

    @property
    def model_names(self):
        return list(self.models.keys())


class SingleModel:
    def __init__(self, name: str, kline_interval: int, direction: str, modules: List):
        self.name = name
        self.kline_interval = kline_interval
        self.direction = direction
        self.modules = modules[:]  # 复制列表

    def describe(self):
        tooltips = "\n".join(["【" + m.name + "】" + m.tooltip() for m in self.modules])
        return (
            f"名称: {self.name}\n"
            f"k线周期: {self.kline_interval} 分钟\n"
            f"方向: {self.direction}\n"
            "---\n"
            "指标:\n"
            f"{tooltips}\n"
            "---"
        )

    def update_value(self):
        # 更新module
        pass
