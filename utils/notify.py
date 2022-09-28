# --coding:utf-8--
from functools import partial
from PySide6.QtWidgets import QMessageBox

choose_metric = lambda parent: QMessageBox.warning(parent, "错误", "请先选择指标!")
fill_model_name = lambda parent: QMessageBox.warning(parent, "错误", "请填写策略名称!")
add_metric = lambda parent: QMessageBox.warning(parent, "错误", "请添加指标!")
