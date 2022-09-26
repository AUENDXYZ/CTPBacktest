# --coding:utf-8--
from pathlib import Path
CURR = Path(__file__).absolute().parent
HOME = CURR.parent
DEFAULT_MODULE = HOME.joinpath("core", "metrics", "default_modules")
USER_MODULE = HOME.joinpath("core", "metrics", "user_modules")
MODULE_MAPPING_NAME = HOME.joinpath("core", "metrics", "module_mapping_name.json")
DB = HOME.joinpath("database")
SETTING_JSON = HOME.joinpath("setting", "settings.json")
