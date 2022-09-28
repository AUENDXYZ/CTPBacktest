# --coding:utf-8--
import loguru
import traceback
import datetime as dt
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from queue import Queue

from PySide6 import QtGui
from PySide6.QtCore import Qt, QThreadPool, QSize, Slot, QTimer, QTime
from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QWidget,
    QCompleter,
    QComboBox,
    QTableWidgetItem,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QDialog,
    QApplication,
    QLineEdit,
    QLabel,
    QCheckBox,
    QTimeEdit,
)
from PySide6.QtGui import QDoubleValidator

from core.metrics.modules_manage import ModuleManager
from core.models.models_manage import ModelManager, SingleModel
from utils.tools import compare_type
from utils import notify
from ui.ui_main import Ui_MainWindow


class StateParams:
    metric_params = []
    metric_conditions = []
    added_modules = []


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.thread_pool = QThreadPool()  # pyside的线程池
        self.timer = QTimer()  # pyside定时器
        self.backend_TP = ThreadPoolExecutor()  # python线程池，防止卡顿
        self.__backtest_running = True  # 后台线程是否运行由此控制

        self.module_manage = ModuleManager()
        self.model_manage = ModelManager()
        self.init()

    def init(self):
        self.bind_actions()
        self.fill_data()

    def bind_actions(self):
        # 关联按键动作
        # nav button action
        self.body_stacked.setCurrentIndex(0)
        self.home_btn.clicked.connect(lambda: self.body_stacked.setCurrentIndex(0))
        self.create_btn.clicked.connect(lambda: self.body_stacked.setCurrentIndex(1))
        self.backtest_btn.clicked.connect(lambda: self.body_stacked.setCurrentIndex(2))
        self.setting_btn.clicked.connect(lambda: self.body_stacked.setCurrentIndex(3))

        # create page action
        self.add_metric_btn.clicked.connect(self.add_metric)
        self.submit_btn.clicked.connect(self.create_model)
        self.metric_combo.currentIndexChanged.connect(self.show_param_condition)

        # backtest page action
        self.backtest_stack.setCurrentIndex(0)
        self.mark_label_color()
        self.stage1_to_next.clicked.connect(lambda: self.mark_label_color(2))
        self.stage1_to_next.clicked.connect(
            lambda: self.backtest_stack.setCurrentIndex(1)
        )
        self.stage2_to_prev.clicked.connect(lambda: self.mark_label_color(1))
        self.stage2_to_prev.clicked.connect(
            lambda: self.backtest_stack.setCurrentIndex(0)
        )
        self.stage2_to_next.clicked.connect(lambda: self.mark_label_color(3))
        self.stage2_to_next.clicked.connect(
            lambda: self.backtest_stack.setCurrentIndex(2)
        )
        self.model_options.currentIndexChanged.connect(self.show_model_detail)
        self.tick_file_btn.clicked.connect(self.select_tick_file)

    def fill_data(self):
        # combobox数据填充到界面
        modules = self.module_manage.module_names
        self.metric_combo.clear()
        self.metric_combo.addItems(["--选择指标--"] + modules)
        models = self.model_manage.model_names
        self.model_options.clear()
        self.model_options.addItems(["--选择策略--"] + models)

    def add_metric(self):
        # 创建策略-将指标添加到策略中
        metric_name = self.metric_combo.currentText()
        if metric_name not in self.module_manage.module_names:
            notify.choose_metric(self)
            return
        module = self.module_manage.modules[metric_name](len(StateParams.added_modules))
        params = {}
        for w in StateParams.metric_params:
            button = w.layout().itemAt(0).widget()
            edit = w.layout().itemAt(2).widget()
            k = button.text()
            v = float(edit.text() or "0")
            params[k] = v
        condition = {}
        for w in StateParams.metric_conditions:
            check = w.layout().itemAt(0).widget()
            button = w.layout().itemAt(1).widget()
            cond = w.layout().itemAt(2).widget()
            edit = w.layout().itemAt(3).widget()
            if check.isChecked():
                k = button.text()
                c = cond.currentText()
                if hasattr(edit, "time"):
                    v = edit.time().toPython()
                else:
                    v = edit.text()
                condition[k] = {
                    "func": partial(compare_type(c), b=v),
                    "tip": [k, c, str(v)],
                }
        module.set_metric_params(**params)
        module.set_condition(**{k: v["func"] for k, v in condition.items()})
        module.set_condition_tip(**{k: v["tip"] for k, v in condition.items()})
        StateParams.added_modules.append(module)
        self.add_metric_tolist(module)

    def add_metric_tolist(self, module):
        # 构造指标小部件并添加到列表中
        metric_widget = self.metric_list_widget(module)
        self.added_layout.addWidget(metric_widget)

    def create_model(self):
        # 创建策略模型
        model_name = self.model_name.text()
        if not model_name:
            notify.fill_model_name(self)
            return
        kline_interval = int(self.kline_spin.text())
        if not StateParams.added_modules:
            notify.add_metric(self)
            return
        direction = "多" if self.duo_radio.isChecked() else "空"
        single_model = SingleModel(model_name, kline_interval, direction, StateParams.added_modules)
        try:
            self.model_manage.add_model(single_model)
        except Exception as e:
            QMessageBox.warning(self, "错误", str(e))
            return
        models = self.model_manage.model_names
        self.model_options.clear()
        self.model_options.addItems(["--选择策略--"] + models)
        QMessageBox.about(self, "成功", "创建成功!")

    def mark_label_color(self, label=1):
        # 上侧文字提示的颜色
        for i in (1, 2, 3):
            if i == label:
                getattr(self, f"stage{i}_label").setStyleSheet("color:black;")
            else:
                getattr(self, f"stage{i}_label").setStyleSheet("color:gray;")

    def show_model_detail(self):
        model_name = self.model_options.currentText()
        self.model_show.clear()
        if model_name in self.model_manage.model_names:
            self.model_show.appendPlainText(self.model_manage.models[model_name].describe())

    def select_tick_file(self):
        # 选择tick文件
        self.tick_file.setText(
            QFileDialog.getOpenFileName(self, filter="Csv File (*.csv);;All Files (*)")[
                0
            ]
            or self.tick_file.text()
        )

    def show_param_condition(self):
        curr = self.metric_combo.currentText()
        if not curr:
            return
        if curr != "--选择指标--" and curr not in self.module_manage.module_names:
            QMessageBox.warning(self, "警告", "当前指标未找到!")
            return
        if curr == "--选择指标--":
            for i in StateParams.metric_params:
                self.params_layout.removeWidget(i)
                i.setParent(None)
            StateParams.metric_params.clear()
            for j in StateParams.metric_conditions:
                self.condition_layout.removeWidget(j)
                j.setParent(None)
            StateParams.metric_conditions.clear()
        else:
            module = self.module_manage.modules[curr]
            # params
            params = module.input_params
            defaults = module.default_params
            for i in StateParams.metric_params:
                self.params_layout.removeWidget(i)
                i.setParent(None)
            StateParams.metric_params.clear()
            for p in params:
                _widget = self.metric_param_widget(p, defaults[p])
                StateParams.metric_params.append(_widget)
                self.params_layout.addWidget(_widget)
            # condition
            output_params = module.output_params
            for i in StateParams.metric_conditions:
                self.condition_layout.removeWidget(i)
                i.setParent(None)
            StateParams.metric_conditions.clear()
            for p in output_params:
                _widget = self.metric_condition_widget(p, 0)
                StateParams.metric_conditions.append(_widget)
                self.condition_layout.addWidget(_widget)
            for p in ["high", "low", "open", "close", "volume"]:
                _widget = self.metric_condition_widget(p, 0, checked=False)
                StateParams.metric_conditions.append(_widget)
                self.condition_layout.addWidget(_widget)
            _widget = self.metric_condition_widget(
                "time", 0, is_time=True, checked=False
            )
            StateParams.metric_conditions.append(_widget)
            self.condition_layout.addWidget(_widget)

    def delete_added_metric(self, module, widget):
        StateParams.added_modules.remove(module)
        widget.setParent(None)
        del widget

    @Slot()
    def metric_param_widget(self, key, value):
        _widget = QWidget()
        _layout = QHBoxLayout()
        _widget.setLayout(_layout)

        button = QPushButton(key)
        button.setStyleSheet("font-weight:bold;border:none")
        button.setContentsMargins(0, 0, 0, 0)
        button.setFixedSize(QSize(80, 18))
        _layout.addWidget(button)

        label = QLabel("=")
        label.setFixedSize(QSize(10, 18))
        label.setContentsMargins(0, 0, 0, 0)
        label.setStyleSheet("border:none;")
        _layout.addWidget(label)

        edit = QLineEdit(str(value))
        edit.setValidator(QDoubleValidator())
        edit.setStyleSheet("border: 1px solid black;")
        edit.setContentsMargins(0, 0, 0, 0)
        edit.setFixedSize(QSize(50, 18))
        _layout.addWidget(edit)

        return _widget

    @Slot()
    def metric_condition_widget(self, key, value, is_time=False, checked=True):
        _widget = QWidget()
        _layout = QHBoxLayout()

        check = QCheckBox()
        check.setChecked(checked)
        check.setFixedSize(QSize(13, 18))
        check.setStyleSheet("border:none;font-weight:bold;")
        _layout.addWidget(check)

        button = QPushButton(key)
        button.setStyleSheet("font-weight:bold; border:none")
        button.setFixedSize(QSize(47, 18))
        _layout.addWidget(button)

        combo = QComboBox()
        combo.addItems([">", "=", "<", "!="])
        combo.setFixedSize(QSize(33, 18))
        combo.setStyleSheet("font-weight:bold;")
        _layout.addWidget(combo)

        if is_time is False:
            edit = QLineEdit(str(value))
            edit.setValidator(QDoubleValidator())
            edit.setStyleSheet("border: 1px solid black;")
            edit.setFixedSize(QSize(80, 18))
            _layout.addWidget(edit)
        else:
            _time = QTimeEdit()
            _time.setTime(QTime(9, 0, 0, 0))
            _time.setStyleSheet("border: 1px solid black;")
            _time.setFixedSize(QSize(80, 18))
            _layout.addWidget(_time)
        _widget.setLayout(_layout)
        return _widget

    @Slot()
    def metric_list_widget(self, module):
        _widget = QWidget()
        _widget.setStyleSheet("border: 1px solid black;background-color:white;")
        _layout = QHBoxLayout()
        _widget.setLayout(_layout)
        _widget.setToolTip(module.tooltip())

        label = QLabel(module.name)
        label.setContentsMargins(0, 0, 0, 0)
        label.setFixedSize(QSize(150, 18))
        _layout.addWidget(label)

        delete = QPushButton("X")
        delete.setContentsMargins(0, 0, 0, 0)
        delete.setFixedSize(QSize(20, 18))
        delete.setStyleSheet(
            "QPushButton::hover {background-color: rgb(151,195,243)}\n"
            "QPushButton::pressed {background-color: white;color: rgb(154,197,244)};"
        )
        delete.clicked.connect(partial(self.delete_added_metric, module, _widget))
        _layout.addWidget(delete)

        return _widget
