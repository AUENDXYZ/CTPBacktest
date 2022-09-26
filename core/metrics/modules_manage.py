# --coding:utf-8--
import sys
import pandas as pd
import numpy as np
from pathlib import Path
from importlib import import_module
from typing import Dict, Optional
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
        self.name = name
        self.path = path
        self.module_type = module_type
        self.input_params = []
        self.default_params = {}
        self.output_params = []
        self.output_default_params = {}
        self.module: Optional[object] = None
        self.results = {}
        self.load()

    def set_input(self, *args, **kwargs):
        self.input_params = list(args)
        self.default_params = {i: 0 for i in args}
        self.input_params += list(kwargs.keys())
        self.default_params.update(kwargs)

    def set_output(self, *args, **kwargs):
        self.output_params = list(args)
        self.output_params += list(kwargs.keys())
        self.output_default_params = kwargs

    def load(self):
        p_path = str(self.path.parent)
        if p_path not in sys.path:
            sys.path.append(p_path)
        self.module = import_module(self.name)
        setattr(self.module, "pd", pd)
        setattr(self.module, "np", np)
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
            self.update_value(**{k: v[:i] for k, v in fake_data.items()})
            self.backtest()
        self.results.clear()
        return True

    def update_value(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self.module, k, v)

    def backtest(self):
        results = getattr(self.module, "method")()
        self.results = results
