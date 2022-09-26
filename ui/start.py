# --coding:utf-8--
import loguru
import traceback
import datetime as dt
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from queue import Queue

from PySide6 import QtGui
from PySide6.QtCore import Qt, QThreadPool, QSize, Slot, QTimer
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
    QDialog,
    QApplication,
    QLineEdit,
)

from core.metrics.modules_manage import ModuleManager

from ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.thread_pool = QThreadPool()  # pyside的线程池
        self.timer = QTimer()  # pyside定时器
        self.backend_TP = ThreadPoolExecutor()  # python线程池，防止卡顿
        self.__backtest_running = True  # 后台线程是否运行由此控制

        self.queue = Queue()  # 此队列用于从服务器获取的数据展示的数据
        self.module_manage = ModuleManager()
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
        self.tick_file_btn.clicked.connect(self.select_tick_file)

    def fill_data(self):
        # 数据填充到界面
        modules = self.module_manage.module_names
        self.metric_combo.addItems([""] + modules)

    def add_metric(self):
        pass

    def create_model(self, checked):
        print(checked)
        pass

    def mark_label_color(self, label=1):
        for i in (1, 2, 3):
            if i == label:
                getattr(self, f"stage{i}_label").setStyleSheet("color:black;")
            else:
                getattr(self, f"stage{i}_label").setStyleSheet("color:gray;")

    def select_tick_file(self):
        self.tick_file.setText(
            QFileDialog.getOpenFileName(
                self, filter="Csv File (*.csv);;All Files (*)"
            )[0]
            or self.tick_file.text()
        )

    def show_param_condition(self):
        curr = self.metric_combo.currentText()
        if not curr:
            return
        if curr not in self.module_manage.module_names:
            QMessageBox.warning(self, "警告", "当前指标未找到!")
            return

