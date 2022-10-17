# --coding:utf-8--
import datetime as dt
from functools import partial

from PySide6.QtCore import (
    Qt,
    QThreadPool,
    QSize,
    Slot,
    QTimer,
    QTime,
    QCoreApplication,
)
from PySide6.QtGui import QDoubleValidator, QIntValidator
from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QWidget,
    QComboBox,
    QTableWidgetItem,
    QPushButton,
    QHBoxLayout,
    QLineEdit,
    QLabel,
    QCheckBox,
    QTimeEdit,
    QSizePolicy,
)

import database.sqlite
import setting
from core.backtest import run_backtest
from core.metrics.modules_manage import ModuleManager
from core.models.models_manage import ModelManager, SingleModel
from ui.ui_main import Ui_MainWindow
from utils import notify
from utils.pyqt_translucent_full_loading_screen_thread import (
    LoadingTranslucentScreen,
    LoadingThread,
)
from utils.tools import compare_type, load_data
from utils.worker import WorkerThread


class StateParams:
    metric_params = []
    metric_conditions = []
    added_modules = []
    selected_model = None
    df = None
    trade_time_range = []
    column_alias = {}


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.loadingTranslucentScreen = LoadingTranslucentScreen(
            parent=self.backtest_pg, description_text="载入中", dot_animation=True
        )
        self.loading_thread = LoadingThread(
            loading_screen=self.loadingTranslucentScreen
        )

        self.thread_pool = QThreadPool()  # pyside的线程池
        self.timer = QTimer()  # pyside定时器

        self.module_manage = ModuleManager()
        self.model_manage = ModelManager(self.module_manage)
        self.backtest_thread = None
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
        self.stage1_to_next.clicked.connect(self.stage1_to_next_action)
        self.stage2_to_prev.clicked.connect(self.stage2_to_prev_action)
        self.stage2_to_next.clicked.connect(self.stage2_to_next_action)
        self.stage3_to_prev.clicked.connect(lambda: self.mark_label_color(2))
        self.stage3_to_prev.clicked.connect(
            lambda: self.backtest_stack.setCurrentIndex(1)
        )
        self.model_options.currentIndexChanged.connect(self.show_model_detail)
        self.tick_file_btn.clicked.connect(self.select_tick_file)
        self.datetime_col.currentIndexChanged.connect(
            partial(self.load_col, label="datetime")
        )
        self.price_col.currentIndexChanged.connect(
            partial(self.load_col, label="price")
        )
        self.volume_col.currentIndexChanged.connect(
            partial(self.load_col, label="volume")
        )
        self.trade_time_add_btn.clicked.connect(self.add_trade_range)
        self.res_clear_btn.clicked.connect(self.clear_res)
        self.res_save_btn.clicked.connect(self.save_res)
        self.end_backtest_btn.clicked.connect(self.end_backtest)

        # thread
        self.loading_thread.loadingSignal.connect(self.load_csv_result)

        # setting
        self.model_delete_btn.clicked.connect(self.model_delete)
        self.dpi_save.clicked.connect(self.change_dpi)
        self.tick_load_rows_btn.clicked.connect(self.change_tick_load_rows)

        # validate
        self.dpi_input.setValidator(QIntValidator(bottom=80, top=200))
        self.tick_load_rows.setValidator(QIntValidator(bottom=1, top=1000000))

        # about
        self.label_about.setText(setting.Setting["about"] + " version:" + setting.Setting["version"])

    def fill_data(self):
        # combobox数据填充到界面
        modules = self.module_manage.module_names
        self.metric_combo.clear()
        self.metric_combo.addItems(["--选择指标--"] + modules)
        self.update_model_combo()
        range1 = [dt.time(9, 1), dt.time(10, 15)]
        w1 = self.trade_range_widget(*range1)
        self.trade_range_layout.addWidget(w1)
        StateParams.trade_time_range.append(range1)
        range2 = [dt.time(10, 31), dt.time(11, 30)]
        w2 = self.trade_range_widget(*range2)
        self.trade_range_layout.addWidget(w2)
        StateParams.trade_time_range.append(range2)
        range3 = [dt.time(13, 31), dt.time(15)]
        w3 = self.trade_range_widget(*range3)
        self.trade_range_layout.addWidget(w3)
        StateParams.trade_time_range.append(range3)
        range4 = [dt.time(21, 1), dt.time(23)]
        w4 = self.trade_range_widget(*range4)
        self.trade_range_layout.addWidget(w4)
        StateParams.trade_time_range.append(range4)

        self.dpi_input.setText(str(setting.Setting["dpi"]))
        self.tick_load_rows.setText(str(setting.Setting["tick_load_rows"]))

    def stage1_to_next_action(self):
        if StateParams.selected_model is None:
            if len(self.model_manage.model_names) == 0:
                notify.err_msg(self, "请先去创建策略")
                return
            else:
                notify.err_msg(self, "请选择策略")
                return
        self.mark_label_color(2)
        self.backtest_stack.setCurrentIndex(1)

    def stage2_to_prev_action(self):
        self.mark_label_color(1)
        self.backtest_stack.setCurrentIndex(0)

    def stage2_to_next_action(self):
        if StateParams.df is None:
            notify.err_msg(self, "请选择tick文件")
            return
        if not StateParams.trade_time_range:
            notify.err_msg(self, "请指定交易时间")
            return
        if len(StateParams.column_alias) < 3:
            notify.err_msg(self, "请指定对应列名")
            return

        self.mark_label_color(3)
        self.backtest_stack.setCurrentIndex(2)
        self.create_backtest_thread()

    def create_backtest_thread(self):
        if self.backtest_thread is not None:
            return
        worker_thread = WorkerThread()
        worker_thread.set_task(run_backtest,
                               StateParams.df,
                               StateParams.selected_model,
                               StateParams.trade_time_range,
                               StateParams.column_alias, )
        worker_thread.result.connect(self.backtest_result)
        worker_thread.finished.connect(self.backtest_complete)
        worker_thread.progress.connect(self.backtest_progress)
        worker_thread.alarm.connect(self.backtest_output)
        worker_thread.error.connect(self.backtest_output)
        self.backtest_thread = worker_thread
        self.backtest_thread.start()
        # worker = Worker(
        #     run_backtest,
        #     StateParams.df,
        #     StateParams.selected_model,
        #     StateParams.trade_time_range,
        #     StateParams.column_alias,
        # )
        # worker.signals.result.connect(self.backtest_result)
        # worker.signals.finished.connect(self.backtest_complete)
        # worker.signals.progress.connect(self.backtest_progress)
        # worker.signals.alarm.connect(self.backtest_output)
        # worker.signals.error.connect(self.backtest_output)
        # self.backtest_thread = worker
        # self.thread_pool.start(worker)

    def end_backtest(self):
        print("end")

    def backtest_result(self, msg):
        print("result", msg)
        pass

    def clear_res(self):
        self.backtest_log.clear()

    def save_res(self):
        file_name = QFileDialog.getSaveFileName(
            self, filter="TXT File (*.txt);;All Files (*)"
        )[0]
        if not file_name:
            return
        text = self.backtest_log.toPlainText()
        try:
            with open(file_name, "w") as f:
                f.write(text)
        except Exception as e:
            notify.err_msg(self, f"写入失败: {str(e)}")

    def backtest_complete(self):
        print("complete")
        self.backtest_thread = None

    def backtest_progress(self, msg):
        print("progress")
        return

    def backtest_output(self, msg):
        print("output")
        self.backtest_log.append(f"[{dt.datetime.now()}] {msg}\n")

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
                    v = float(edit.text())
                condition[k] = {
                    "func": lambda x: compare_type(c)(x, v),
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

    def update_model_combo(self):
        models = self.model_manage.model_names
        self.model_options.clear()
        self.model_options.addItems(["--选择策略--"] + models)
        self.model_delete_combo.clear()
        self.model_delete_combo.addItems(["--选择策略--"] + models)

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
        single_model = SingleModel(
            model_name, kline_interval, direction, StateParams.added_modules
        )
        try:
            self.model_manage.add_model(single_model)
        except Exception as e:
            QMessageBox.warning(self, "错误", str(e))
            return
        self.update_model_combo()
        notify.create_success(self)

    def model_delete(self):
        model = self.model_delete_combo.currentText()
        if model in self.model_manage.models:
            self.model_manage.models.pop(model)
            database.sqlite.Models.get(name=model).delete_instance()
            self.update_model_combo()
            self.backtest_stack.setCurrentIndex(0)
            notify.success_msg(self, f"{model} 已删除")

    def change_dpi(self):
        dpi = self.dpi_input.text()
        dpi = int(dpi)
        if dpi < 60:
            notify.err_msg(self, msg="dpi不可以小于60")
            return
        setting.write_setting("dpi", str(dpi))
        notify.success_msg(self, "修改成功\n重启后生效")

    def change_tick_load_rows(self):
        rows = self.tick_load_rows.text()
        rows = int(rows)
        if rows < 1:
            notify.err_msg(self, msg="输入错误")
            return
        setting.write_setting("tick_load_rows", rows)
        notify.success_msg(self, "tick表显示行数 修改成功")

    def mark_label_color(self, label=1):
        # 上侧文字提示的颜色
        for i in (1, 2, 3):
            if i == label:
                getattr(self, f"stage{i}_label").setStyleSheet("color:white;")
            else:
                getattr(self, f"stage{i}_label").setStyleSheet("color:gray;")

    def show_model_detail(self):
        model_name = self.model_options.currentText()
        self.model_show.clear()
        StateParams.selected_model = None
        if model_name in self.model_manage.model_names:
            StateParams.selected_model = self.model_manage.models[model_name]
            self.model_show.setText(self.model_manage.models[model_name].describe())

    def load_col(self, col_index, label):
        if label == "datetime":
            text = self.datetime_col.currentText()
        elif label == "price":
            text = self.price_col.currentText()
        elif label == "volume":
            text = self.volume_col.currentText()
        else:
            return
        if text == "--请选择--":
            if label in StateParams.column_alias:
                del StateParams.column_alias[label]
        else:
            StateParams.column_alias[label] = text

    def add_trade_range(self):
        trade_range = [
            self.trade_time_add1.time().toPython(),
            self.trade_time_add2.time().toPython(),
        ]
        if trade_range in StateParams.trade_time_range:
            return
        w = self.trade_range_widget(*trade_range)
        self.trade_range_layout.addWidget(w)
        StateParams.trade_time_range.append(trade_range)

    def delete_trade_range(self, w, trade_range):
        if trade_range in StateParams.trade_time_range:
            StateParams.trade_time_range.remove(trade_range)
        w.setParent(None)
        del w

    def select_tick_file(self):
        # 选择tick文件
        tick_file_name = QFileDialog.getOpenFileName(
            self, filter="Csv File (*.csv);;All Files (*)"
        )[0]
        if not tick_file_name:
            return
        if not tick_file_name.lower().endswith(".csv"):
            notify.choose_csv(self)
            return
        self.loading_thread.start(lambda parent: self.load_csv(tick_file_name, parent))

    def load_csv(self, file_path, thread):
        try:
            df = load_data(file_path)
        except Exception as e:
            thread.loadingSignal.emit(str(e))
            return
        # lost_cols = []
        # for name in ["datetime", "open", "close", "high", "low", "volume"]:
        #     if name not in df.columns:
        #         lost_cols.append(name)
        # if lost_cols:
        #     thread.loadingSignal.emit('缺少"' + " ".join(lost_cols) + '"列\n请修改列名后重试')
        #     return

        self.tick_table.clearContents()
        for i in range(self.tick_table.rowCount() - 1, -1, -1):
            self.tick_table.removeRow(i)
        for i in range(self.tick_table.columnCount() - 1, -1, -1):
            self.tick_table.removeColumn(i)
        StateParams.df = None
        n = len(df.columns)
        for i in range(n):
            self.tick_table.insertColumn(i)
        self.tick_table.setColumnCount(n)
        self.tick_table.setHorizontalHeaderLabels(df.columns)
        self.tick_table.setRowCount(min(len(df), int(setting.Setting["tick_load_rows"])))
        row_index = 0
        for _, row in df.iterrows():
            # self.tick_table.insertRow(row_index)
            if row_index > setting.Setting["tick_load_rows"]:
                break
            for i in range(n):
                self.tick_table.setItem(
                    row_index, i, QTableWidgetItem(str(row[df.columns[i]]))
                )
            row_index += 1

        self.tick_file.setText(file_path)
        StateParams.df = df
        self.datetime_col.clear()
        self.price_col.clear()
        self.volume_col.clear()
        columns = ["--请选择--"] + list(df.columns)
        self.datetime_col.addItems(columns)
        if "时间" in columns:
            self.datetime_col.setCurrentIndex(columns.index("时间"))
        self.price_col.addItems(columns)
        if "最新" in columns:
            self.price_col.setCurrentIndex(columns.index("最新"))
        self.volume_col.addItems(columns)
        if "成交量" in columns:
            self.volume_col.setCurrentIndex(columns.index("成交量"))

    def load_csv_result(self, result):
        if result:
            notify.err(self, result)

    def show_param_condition(self):
        curr = self.metric_combo.currentText()
        if not curr:
            return
        if curr != "--选择指标--" and curr not in self.module_manage.module_names:
            notify.not_found_metric(self)
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
        from utils.style import STYLESHEET
        _widget = QWidget()
        _widget.setStyleSheet(STYLESHEET)
        _layout = QHBoxLayout()
        _widget.setLayout(_layout)

        button = QPushButton(key)
        # button.setStyleSheet("font-weight:bold;border:none")
        button.setContentsMargins(0, 0, 0, 0)
        button.setFixedSize(QSize(90, 18))
        _layout.addWidget(button)

        label = QLabel("=")
        label.setFixedSize(QSize(10, 18))
        label.setContentsMargins(0, 0, 0, 0)
        # label.setStyleSheet("border:none;")
        _layout.addWidget(label)

        edit = QLineEdit(str(value))
        edit.setValidator(QDoubleValidator())
        # edit.setStyleSheet("border: 1px solid black;")
        edit.setContentsMargins(0, 0, 0, 0)
        edit.setFixedSize(QSize(50, 18))
        _layout.addWidget(edit)

        return _widget

    @Slot()
    def metric_condition_widget(self, key, value, is_time=False, checked=True):
        from utils.style import STYLESHEET
        _widget = QWidget()
        _widget.setStyleSheet(STYLESHEET)

        _layout = QHBoxLayout()

        check = QCheckBox()
        check.setChecked(checked)
        check.setFixedSize(QSize(15, 18))
        # check.setStyleSheet("border:none;font-weight:bold;")
        _layout.addWidget(check)

        button = QPushButton(key)
        # button.setStyleSheet("font-weight:bold; border:none")
        button.setFixedSize(QSize(50, 18))
        _layout.addWidget(button)

        combo = QComboBox()
        combo.addItems([">", "=", "<", "!="])
        combo.setFixedSize(QSize(33, 18))
        # combo.setStyleSheet("font-weight:bold;")
        _layout.addWidget(combo)

        if is_time is False:
            edit = QLineEdit(str(value))
            edit.setValidator(QDoubleValidator())
            # edit.setStyleSheet("border: 1px solid black;")
            edit.setFixedSize(QSize(80, 18))
            _layout.addWidget(edit)
        else:
            _time = QTimeEdit()
            _time.setTime(QTime(9, 0, 0, 0))
            # _time.setStyleSheet("border: 1px solid black;")
            _time.setFixedSize(QSize(80, 18))
            _layout.addWidget(_time)
        _widget.setLayout(_layout)
        return _widget

    @Slot()
    def metric_list_widget(self, module):
        from utils.style import STYLESHEET
        _widget = QWidget()
        _widget.setStyleSheet(STYLESHEET)
        _layout = QHBoxLayout()
        _widget.setLayout(_layout)
        _widget.setToolTip(module.tooltip())

        label = QPushButton(module.name)
        label.setContentsMargins(0, 0, 0, 0)
        label.setFixedSize(QSize(200, 20))
        _layout.addWidget(label)

        delete = QPushButton("X")
        delete.setContentsMargins(0, 0, 0, 0)
        delete.setFixedSize(QSize(20, 20))
        delete.setStyleSheet(
            "QPushButton {color: red}\n"
            "QPushButton::hover {background-color: rgb(151,195,243)}\n"
            "QPushButton::pressed {background-color: white;color: rgb(154,197,244)};"
        )
        _module = module
        delete.clicked.connect(partial(self.delete_added_metric, _module, _widget))
        _layout.addWidget(delete)

        return _widget

    @Slot()
    def trade_range_widget(self, start_time, end_time):
        from utils.style import STYLESHEET
        _widget = QWidget()
        _widget.setStyleSheet(STYLESHEET)
        _layout = QHBoxLayout()
        _widget.setLayout(_layout)

        #  时区+8
        time1 = QTimeEdit()
        time1.setTime(QTime(start_time.hour, start_time.minute))
        time1.setContentsMargins(0, 0, 0, 0)
        time1.setDisplayFormat(QCoreApplication.translate("MainWindow", "hh:mm", None))
        time1.setDisabled(True)
        _layout.addWidget(time1)

        label = QLabel("-")
        label.setContentsMargins(0, 0, 0, 0)
        label.setAlignment(Qt.AlignCenter)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label.hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        _layout.addWidget(label)

        time2 = QTimeEdit()
        time2.setTime(QTime(end_time.hour, end_time.minute))
        time2.setContentsMargins(0, 0, 0, 0)
        time2.setDisplayFormat(QCoreApplication.translate("MainWindow", "hh:mm", None))
        time2.setDisabled(True)
        _layout.addWidget(time2)

        delete = QPushButton("X")
        delete.setContentsMargins(0, 0, 0, 0)
        delete.setFixedSize(QSize(20, 18))
        delete.setStyleSheet(
            "QPushButton {color: red}\n"
            "QPushButton::hover {background-color: rgb(151,195,243)}\n"
            "QPushButton::pressed {background-color: white;color: rgb(154,197,244)};"
        )
        delete.clicked.connect(
            partial(
                self.delete_trade_range, w=_widget, trade_range=[start_time, end_time]
            )
        )
        _layout.addWidget(delete)

        return _widget
