import time
from typing import Optional
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QWidget

from utils.pyqt_translucent_full_loading_screen_thread.loadingTranslucentScreen import LoadingTranslucentScreen


class LoadingThread(QThread):
    loadingSignal = Signal(str)

    def __init__(self, loading_screen: LoadingTranslucentScreen, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__loadingTranslucentScreen = loading_screen
        self.__loadingTranslucentScreen.setParentThread(self)
        self.started.connect(self.__loadingTranslucentScreen.start)
        self.finished.connect(self.__loadingTranslucentScreen.stop)
        self.started.connect(self.__loadingTranslucentScreen.makeParentDisabledDuringLoading)
        self.finished.connect(self.__loadingTranslucentScreen.makeParentDisabledDuringLoading)
        self.task = None

    def start(self, task, *args, **kwargs) -> None:
        self.task = task
        super(LoadingThread, self).start(*args, **kwargs)

    def run(self):
        self.task(self)
