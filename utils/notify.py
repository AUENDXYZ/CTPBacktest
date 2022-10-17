# --coding:utf-8--
from functools import partial
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QTimer
from PySide6.QtCore import Qt

choose_metric = lambda parent: QMessageBox.warning(parent, "错误", "请先选择指标!")
fill_model_name = lambda parent: QMessageBox.warning(parent, "错误", "请填写策略名称!")
add_metric = lambda parent: QMessageBox.warning(parent, "错误", "请添加指标!")
create_success = lambda parent: QMessageBox.about(parent, "成功", "创建成功!")
not_found_metric = lambda parent: QMessageBox.warning(parent, "警告", "当前指标未找到!")
choose_csv = lambda parent: QMessageBox.warning(parent, "警告", "请选择csv文件!")
err = lambda parent, msg: QMessageBox.warning(parent, "错误", f"出现错误 {msg}")
lost_cols = lambda parent, msg: QMessageBox.warning(parent, "错误", f"缺少字段 {msg}\n请修改字段名称后再重试")
err_msg = lambda parent, msg: QMessageBox.warning(parent, "错误", msg)
success_msg = lambda parent, msg: QMessageBox.information(parent, "成功", msg)
auto_close_info = lambda parent, msg: TimerMessageBox(msg, parent=parent).exec()


class TimerMessageBox(QMessageBox):
    def __init__(self, msg, timeout=3, parent=None):
        super(TimerMessageBox, self).__init__(None)
        self.setText(msg)
        self.setStandardButtons(QMessageBox.NoButton)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("font-weight: bold")
        self.time_to_wait = timeout
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.changeContent)
        self.timer.start()

    def changeContent(self):
        self.time_to_wait -= 1
        if self.time_to_wait <= 0:
            self.close()

    def closeEvent(self, event) -> None:
        self.timer.stop()
        event.accept()
