# --coding:utf-8--
import os
import sys

from PySide6 import QtWidgets

from ui.start import MainWindow

if __name__ == '__main__':
    from setting import Setting
    # create the application and the main window
    os.environ["QT_FONT_DPI"] = Setting["dpi"]
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    # run
    window.show()
    sys.exit(app.exec())
