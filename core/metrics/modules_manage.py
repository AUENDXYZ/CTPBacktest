# --coding:utf-8--
import sys
import talib
import pandas as pd
import numpy as np
from pathlib import Path
from importlib import import_module
from typing import Dict, Optional, List
from copy import deepcopy
from utils.tools import (
    get_python_files,
    gen_fake_values,
    get_module_module_name,
    get_module_mapping_name,
    set_module_mapping_name,
    remove_module_mapping_name,
)
from utils import paths


class ModuleManager:
    def __init__(self):
        self.modules: Dict[str, "SingleModule"] = {}
        self.load_modules()

    @property
    def module_names(self):
        return list(self.modules.keys())

    def load_user_module(self, module_name):
        # 载入指定module
        self._load_typed_module(module_name, paths.USER_MODULE, "user")

    def load_default_module(self, module_name):
        # 载入指定module
        self._load_typed_module(module_name, paths.DEFAULT_MODULE, "default")

    def _load_typed_module(self, module_name, module_path, module_type):
        md5_name = get_module_mapping_name(module_name)
        files = get_python_files(module_path)
        if md5_name not in files:
            raise FileNotFoundError(f"{module_name} 不存在")
        self._load_module(module_name, files[md5_name], module_type)

    def load_modules(self):
        # 载入所有module
        for k, v in get_python_files(paths.DEFAULT_MODULE).items():
            self._load_module(get_module_module_name(k), v, "default")
        for k, v in get_python_files(paths.USER_MODULE).items():
            self._load_module(get_module_module_name(k), v, "user")

    def _load_module(self, module_name, module_path, module_type=None):
        # 载入module的实例方法
        module = SingleModule(module_name, module_path, module_type=module_type)
        self.modules[module_name] = module

    def write_module(self, module_name, content):
        md5_name = set_module_mapping_name(module_name)
        if (module_name in self.modules) or (md5_name in self.modules):
            raise ValueError(f"{module_name} 名称重复")
        path = paths.USER_MODULE.joinpath(f"{md5_name}.py")
        if path.exists():
            raise ValueError("存在重复文件")
        path.write_text(content, encoding="utf-8")
        # self.load_modules()
        self._load_module(module_name, path, "user")

    def delete_module(self, module_name):
        # 删除指定module
        if module_name in self.modules:
            self.modules.pop(module_name)
        remove_module_mapping_name(module_name)


class SingleModule:
    def __init__(self, name: str, path: Path, module_type: str):
        self.name = name  # 名称
        self.path = path  # 路径
        self.module_type = module_type  # default/user
        self.input_params = []  # 输入参数
        self.default_params = {}  # 输入参数的默认值{参数名:参数默认值}
        self.output_params = []  # 输出参数名列表
        self.output_default_params = {}  # 允许设置输出参数值为固定值{参数名: 值}
        self.module: Optional[object] = None  # 真实的module
        self.load()

    def __call__(self, serial_name):
        # init中的参数对每个同类的module来说都是相同的, 这里的参数每个module是用户单独设置的
        class Module:
            def __init__(self, serial_name: str, parent: SingleModule):
                self.result = {}  # module的最新计算结果
                self.metric_params = {}  # 回测时真正使用的参数值
                self.condition = {}  # 回测时的条件判断
                self.condition_tip = {}
                self.serial_name = serial_name
                self.name = parent.name
                self.input_params = parent.input_params
                self.default_params = parent.default_params
                self.output_params = parent.output_params
                self.output_default_params = parent.default_params
                self.module = parent.module

            def __set(self, attribute, clear, items):
                if clear:
                    attribute.clear()
                for k, v in items.items():
                    attribute[k] = v

            def set_metric_params(self, clear=False, **kwargs):
                self.__set(self.metric_params, clear, kwargs)
                self.update_value(**kwargs)

            def set_condition(self, clear=False, **kwargs):
                self.__set(self.condition, clear, kwargs)

            def set_condition_tip(self, clear=False, **kwargs):
                self.__set(self.condition_tip, clear, kwargs)

            def update_value(self, **kwargs):
                # 将数值更新到module中, 比如high, low, open, close等值
                for k, v in kwargs.items():
                    setattr(self.module, k, v)

            def remove_value(self, *args):
                # 清除属性
                for k in args:
                    delattr(self.module, k)

            def backtest(self):
                # 计算
                result = getattr(self.module, "method")()
                result["datetime"] = getattr(self.module, "datetime")[-1]
                self.result = result

            def catch_condition(self):
                for k, v in self.result.items():
                    if k in self.condition and self.condition[k](v):
                        return True
                return False

            def tooltip(self):
                tooltip = (
                        "\n参数\n"
                        + "\n".join([f"{k}={v}" for k, v in self.metric_params.items()])
                        + "\n条件\n"
                        + "\n".join(["".join(v) for v in self.condition_tip.values()])
                )
                return tooltip

        return Module(str(serial_name), self)

    def set_input(self, *args, **kwargs):
        # 回调到module中
        self.input_params = list(args)
        self.default_params = {i: 0 for i in args}
        self.input_params += list(kwargs.keys())
        self.default_params.update(kwargs)

    def set_output(self, *args, **kwargs):
        # 回调到module中
        self.output_params = list(args)
        self.output_params += list(kwargs.keys())
        self.output_default_params = kwargs

    def load(self):
        # 载入module
        p_path = str(self.path.parent)
        if p_path not in sys.path:
            sys.path.append(p_path)
        self.module = import_module(self.name)
        setattr(self.module, "pd", pd)
        setattr(self.module, "np", np)
        setattr(self.module, "talib", talib)
        setattr(self.module, "set_input", self.set_input)
        setattr(self.module, "set_output", self.set_output)
        getattr(self.module, "init")()
        for k, v in self.default_params.items():
            setattr(self.module, k, v)

    def test(self):
        # 测试模型是否有错
        getattr(self.module, "method")
        fake_data = gen_fake_values()
        for i in range(1, len(fake_data["datetime"]) + 1):
            for k, v in fake_data.items():
                setattr(self.module, k, v)
            getattr(self.module, "method")()
        for k in list(fake_data.keys()):
            delattr(self.module, k)
        return True
