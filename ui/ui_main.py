# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTableView,
    QTableWidget, QTableWidgetItem, QTextBrowser, QToolButton,
    QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(990, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nav_widget = QWidget(self.centralwidget)
        self.nav_widget.setObjectName(u"nav_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nav_widget.sizePolicy().hasHeightForWidth())
        self.nav_widget.setSizePolicy(sizePolicy1)
        self.nav_widget.setMinimumSize(QSize(120, 0))
        self.nav_widget.setMaximumSize(QSize(120, 16777215))
        self.nav_widget.setSizeIncrement(QSize(120, 0))
        self.nav_widget.setStyleSheet(u"padding:0;\n"
"border-right: 1px solid rgb(151,195,243);")
        self.verticalLayout = QVBoxLayout(self.nav_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QRadioButton(self.nav_widget)
        self.home_btn.setObjectName(u"home_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.home_btn.sizePolicy().hasHeightForWidth())
        self.home_btn.setSizePolicy(sizePolicy2)
        self.home_btn.setMinimumSize(QSize(80, 30))
        self.home_btn.setMaximumSize(QSize(160, 30))
        self.home_btn.setSizeIncrement(QSize(160, 30))
        self.home_btn.setBaseSize(QSize(80, 30))
        self.home_btn.setStyleSheet(u"QRadioButton {\n"
"font-weight: bold;\n"
"border-radius: 5px;\n"
"}\n"
"QRadioButton::indicator {\n"
"   width: 0px;\n"
"   height: 0px;\n"
"}\n"
"QRadioButton::hover {\n"
"background-color:rgb(154,197,244);\n"
"}\n"
"QRadioButton::checked {\n"
"background-color:rgb(12,57,106);\n"
"color: white;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/nav_btn/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon)
        self.home_btn.setChecked(True)

        self.verticalLayout.addWidget(self.home_btn)

        self.create_btn = QRadioButton(self.nav_widget)
        self.create_btn.setObjectName(u"create_btn")
        sizePolicy2.setHeightForWidth(self.create_btn.sizePolicy().hasHeightForWidth())
        self.create_btn.setSizePolicy(sizePolicy2)
        self.create_btn.setMinimumSize(QSize(80, 30))
        self.create_btn.setMaximumSize(QSize(160, 30))
        self.create_btn.setSizeIncrement(QSize(160, 30))
        self.create_btn.setBaseSize(QSize(80, 30))
        self.create_btn.setStyleSheet(u"QRadioButton {\n"
"font-weight: bold;\n"
"border-radius: 5px;\n"
"}\n"
"QRadioButton::indicator {\n"
"   width: 0px;\n"
"   height: 0px;\n"
"}\n"
"QRadioButton::hover {\n"
"background-color:rgb(154,197,244);\n"
"}\n"
"QRadioButton::checked {\n"
"background-color:rgb(12,57,106);\n"
"color: white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/nav_btn/create.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.create_btn.setIcon(icon1)

        self.verticalLayout.addWidget(self.create_btn)

        self.backtest_btn = QRadioButton(self.nav_widget)
        self.backtest_btn.setObjectName(u"backtest_btn")
        sizePolicy2.setHeightForWidth(self.backtest_btn.sizePolicy().hasHeightForWidth())
        self.backtest_btn.setSizePolicy(sizePolicy2)
        self.backtest_btn.setMinimumSize(QSize(80, 30))
        self.backtest_btn.setMaximumSize(QSize(160, 30))
        self.backtest_btn.setSizeIncrement(QSize(160, 30))
        self.backtest_btn.setBaseSize(QSize(80, 30))
        self.backtest_btn.setStyleSheet(u"QRadioButton {\n"
"font-weight: bold;\n"
"border-radius: 5px;\n"
"}\n"
"QRadioButton::indicator {\n"
"   width: 0px;\n"
"   height: 0px;\n"
"}\n"
"QRadioButton::hover {\n"
"background-color:rgb(154,197,244);\n"
"}\n"
"QRadioButton::checked {\n"
"background-color:rgb(12,57,106);\n"
"color: white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/nav_btn/backtest.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backtest_btn.setIcon(icon2)

        self.verticalLayout.addWidget(self.backtest_btn)

        self.setting_btn = QRadioButton(self.nav_widget)
        self.setting_btn.setObjectName(u"setting_btn")
        sizePolicy2.setHeightForWidth(self.setting_btn.sizePolicy().hasHeightForWidth())
        self.setting_btn.setSizePolicy(sizePolicy2)
        self.setting_btn.setMinimumSize(QSize(80, 30))
        self.setting_btn.setMaximumSize(QSize(160, 30))
        self.setting_btn.setSizeIncrement(QSize(160, 30))
        self.setting_btn.setBaseSize(QSize(80, 30))
        self.setting_btn.setStyleSheet(u"QRadioButton {\n"
"font-weight: bold;\n"
"border-radius: 5px;\n"
"}\n"
"QRadioButton::indicator {\n"
"   width: 0px;\n"
"   height: 0px;\n"
"}\n"
"QRadioButton::hover {\n"
"background-color:rgb(154,197,244);\n"
"}\n"
"QRadioButton::checked {\n"
"background-color:rgb(12,57,106);\n"
"color: white;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/nav_btn/setting.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_btn.setIcon(icon3)

        self.verticalLayout.addWidget(self.setting_btn)

        self.verticalSpacer = QSpacerItem(20, 339, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.nav_widget)

        self.body_widget = QWidget(self.centralwidget)
        self.body_widget.setObjectName(u"body_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(8)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.body_widget.sizePolicy().hasHeightForWidth())
        self.body_widget.setSizePolicy(sizePolicy3)
        self.body_widget.setStyleSheet(u"padding:0;\n"
"background: rgb(243,243,243);")
        self.horizontalLayout_2 = QHBoxLayout(self.body_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.body_stacked = QStackedWidget(self.body_widget)
        self.body_stacked.setObjectName(u"body_stacked")
        sizePolicy.setHeightForWidth(self.body_stacked.sizePolicy().hasHeightForWidth())
        self.body_stacked.setSizePolicy(sizePolicy)
        self.home_pg = QWidget()
        self.home_pg.setObjectName(u"home_pg")
        self.pushButton_3 = QPushButton(self.home_pg)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(370, 10, 75, 24))
        self.body_stacked.addWidget(self.home_pg)
        self.create_pg = QWidget()
        self.create_pg.setObjectName(u"create_pg")
        self.horizontalLayout_3 = QHBoxLayout(self.create_pg)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.create_pg)
        self.frame.setObjectName(u"frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setStyleSheet(u"border-radius: 10%; \n"
"padding: 0;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"border-radius: 10%; \n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.metric_combo = QComboBox(self.groupBox)
        self.metric_combo.setObjectName(u"metric_combo")
        self.metric_combo.setStyleSheet(u"background-color:white;")

        self.verticalLayout_4.addWidget(self.metric_combo)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(3)
        sizePolicy5.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy5)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"border-radius: 10%; ")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 18, 0, 0)
        self.scrollArea_2 = QScrollArea(self.groupBox_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"border-radius:10%;")
        self.scrollArea_2.setWidgetResizable(True)
        self.params_area = QWidget()
        self.params_area.setObjectName(u"params_area")
        self.params_area.setGeometry(QRect(0, 0, 204, 101))
        self.scrollArea_2.setWidget(self.params_area)

        self.horizontalLayout_9.addWidget(self.scrollArea_2)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(5)
        sizePolicy6.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy6)
        self.groupBox_3.setFont(font)
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 18, 0, 0)
        self.scrollArea_3 = QScrollArea(self.groupBox_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"border-radius:10%;")
        self.scrollArea_3.setWidgetResizable(True)
        self.condition_area = QWidget()
        self.condition_area.setObjectName(u"condition_area")
        self.condition_area.setGeometry(QRect(0, 0, 204, 181))
        self.scrollArea_3.setWidget(self.condition_area)

        self.horizontalLayout_10.addWidget(self.scrollArea_3)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy7)
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(86, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.add_metric_btn = QPushButton(self.widget)
        self.add_metric_btn.setObjectName(u"add_metric_btn")
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.add_metric_btn.sizePolicy().hasHeightForWidth())
        self.add_metric_btn.setSizePolicy(sizePolicy8)
        self.add_metric_btn.setMaximumSize(QSize(100, 50))
        self.add_metric_btn.setFont(font)
        self.add_metric_btn.setLayoutDirection(Qt.RightToLeft)
        self.add_metric_btn.setStyleSheet(u"QPushButton{border-radius: 10%; \n"
"border: 2px solid rgb(154,197,244);\n"
"background-color:white;}\n"
"QPushButton::hover {\n"
"background-color: rgb(154,197,244);\n"
"}\n"
"QPushButton::pressed {\n"
"background-color: white;\n"
"color:rgb(154,197,244)\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/create/to_right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_metric_btn.setIcon(icon4)

        self.horizontalLayout_7.addWidget(self.add_metric_btn)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.create_pg)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(1)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy9)
        self.frame_2.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"padding: 0;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(100, 20))
        self.pushButton_2.setMaximumSize(QSize(1000, 50))
        self.pushButton_2.setBaseSize(QSize(100, 20))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_2.setStyleSheet(u"border-radius: 10%; \n"
"border: 2px solid rgb(154,197,244);\n"
"background-color: white;")
        icon5 = QIcon()
        icon5.addFile(u":/create/clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.toolButton = QToolButton(self.frame_2)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy2.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy2)
        self.toolButton.setMaximumSize(QSize(1000, 20))
        self.toolButton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.toolButton.setLayoutDirection(Qt.LeftToRight)
        self.toolButton.setStyleSheet(u"border: none;\n"
"width: 100%;\n"
"align-items:center;")
        icon6 = QIcon()
        icon6.addFile(u":/create/down_continue.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon6)

        self.verticalLayout_2.addWidget(self.toolButton)

        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.widget_2.setMinimumSize(QSize(100, 40))
        self.widget_2.setMaximumSize(QSize(1000, 50))
        self.widget_2.setSizeIncrement(QSize(0, 0))
        self.widget_2.setBaseSize(QSize(500, 20))
        self.widget_2.setStyleSheet(u"border-radius: 10%; \n"
"border: 2px solid rgb(154,197,244);\n"
"background-color: white;")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.kline_spin = QSpinBox(self.widget_2)
        self.kline_spin.setObjectName(u"kline_spin")
        sizePolicy2.setHeightForWidth(self.kline_spin.sizePolicy().hasHeightForWidth())
        self.kline_spin.setSizePolicy(sizePolicy2)
        self.kline_spin.setMaximumSize(QSize(100, 20))
        self.kline_spin.setFont(font)
        self.kline_spin.setStyleSheet(u"border: 1px solid rgb(154,197,244);\n"
"border-radius: 5%;\n"
"background-color:white;")
        self.kline_spin.setMinimum(1)
        self.kline_spin.setMaximum(1200)
        self.kline_spin.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_4.addWidget(self.kline_spin)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(2)
        sizePolicy10.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy10)
        self.label.setMaximumSize(QSize(100, 50))
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: none;")

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.toolButton_2 = QToolButton(self.frame_2)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy2.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy2)
        self.toolButton_2.setMaximumSize(QSize(1000, 20))
        self.toolButton_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.toolButton_2.setLayoutDirection(Qt.LeftToRight)
        self.toolButton_2.setStyleSheet(u"border: none;\n"
"width: 100%;\n"
"align-items:center;")
        self.toolButton_2.setIcon(icon6)

        self.verticalLayout_2.addWidget(self.toolButton_2)

        self.widget_aera = QWidget(self.frame_2)
        self.widget_aera.setObjectName(u"widget_aera")
        sizePolicy11 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(4)
        sizePolicy11.setHeightForWidth(self.widget_aera.sizePolicy().hasHeightForWidth())
        self.widget_aera.setSizePolicy(sizePolicy11)
        self.widget_aera.setMinimumSize(QSize(0, 30))
        self.widget_aera.setMaximumSize(QSize(1000, 1000))
        self.widget_aera.setSizeIncrement(QSize(0, 50))
        self.widget_aera.setStyleSheet(u"QWidget {\n"
"border-radius: 10%; \n"
"border: 2px solid rgb(154,197,244);\n"
"background: white;\n"
"}")
        self.widget_area = QHBoxLayout(self.widget_aera)
        self.widget_area.setObjectName(u"widget_area")
        self.scrollArea = QScrollArea(self.widget_aera)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border-color:rgb(243,243,243);\n"
"background-color: rgb(243,243,243);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 276, 108))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.widget_area.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.widget_aera)

        self.toolButton_3 = QToolButton(self.frame_2)
        self.toolButton_3.setObjectName(u"toolButton_3")
        sizePolicy2.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy2)
        self.toolButton_3.setMaximumSize(QSize(1000, 20))
        self.toolButton_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.toolButton_3.setLayoutDirection(Qt.LeftToRight)
        self.toolButton_3.setStyleSheet(u"border: none;\n"
"width: 100%;\n"
"align-items:center;")
        self.toolButton_3.setIcon(icon6)

        self.verticalLayout_2.addWidget(self.toolButton_3)

        self.widget_3 = QWidget(self.frame_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.widget_3.setMaximumSize(QSize(1000, 50))
        self.widget_3.setStyleSheet(u"QWidget {\n"
"border-radius: 10%; \n"
"border: 2px solid rgb(154,197,244);\n"
"background-color: white;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy10.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy10)
        self.label_2.setMaximumSize(QSize(100, 50))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border: none;")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.kong_radio = QRadioButton(self.widget_3)
        self.kong_radio.setObjectName(u"kong_radio")
        self.kong_radio.setFont(font)
        self.kong_radio.setStyleSheet(u"border:none;")
        self.kong_radio.setChecked(True)

        self.horizontalLayout_5.addWidget(self.kong_radio)

        self.duo_radio = QRadioButton(self.widget_3)
        self.duo_radio.setObjectName(u"duo_radio")
        self.duo_radio.setFont(font)
        self.duo_radio.setStyleSheet(u"border: none;")

        self.horizontalLayout_5.addWidget(self.duo_radio)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.widget_4 = QWidget(self.frame_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.widget_4.setMaximumSize(QSize(1000, 50))
        self.widget_4.setStyleSheet(u"border-radius: 10%; \n"
"border: 2px solid rgb(154,197,244);\n"
"background-color: white;")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy10.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy10)
        self.label_3.setMaximumSize(QSize(100, 50))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"border: none;")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.strategy_name = QLineEdit(self.widget_4)
        self.strategy_name.setObjectName(u"strategy_name")

        self.horizontalLayout_6.addWidget(self.strategy_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.submit_btn = QPushButton(self.widget_4)
        self.submit_btn.setObjectName(u"submit_btn")
        sizePolicy8.setHeightForWidth(self.submit_btn.sizePolicy().hasHeightForWidth())
        self.submit_btn.setSizePolicy(sizePolicy8)
        self.submit_btn.setMinimumSize(QSize(60, 0))
        self.submit_btn.setMaximumSize(QSize(100, 50))
        self.submit_btn.setFont(font)
        self.submit_btn.setStyleSheet(u"QPushButton::hover {\n"
"background-color: rgb(154,197,244);\n"
"}\n"
"QPushButton::pressed {\n"
"background-color: white;\n"
"color: rgb(154,197,244)\n"
"}")

        self.horizontalLayout_6.addWidget(self.submit_btn)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.create_pg)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.create_tips = QTextBrowser(self.frame_3)
        self.create_tips.setObjectName(u"create_tips")
        sizePolicy8.setHeightForWidth(self.create_tips.sizePolicy().hasHeightForWidth())
        self.create_tips.setSizePolicy(sizePolicy8)
        self.create_tips.setStyleSheet(u"border-radius:10%;")

        self.horizontalLayout_8.addWidget(self.create_tips)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.body_stacked.addWidget(self.create_pg)
        self.backtest_pg = QWidget()
        self.backtest_pg.setObjectName(u"backtest_pg")
        sizePolicy.setHeightForWidth(self.backtest_pg.sizePolicy().hasHeightForWidth())
        self.backtest_pg.setSizePolicy(sizePolicy)
        self.horizontalLayout_13 = QHBoxLayout(self.backtest_pg)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_4 = QFrame(self.backtest_pg)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 9, -1, -1)
        self.widget_5 = QWidget(self.frame_4)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy12 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy12)
        self.widget_5.setMinimumSize(QSize(100, 20))
        self.widget_5.setMaximumSize(QSize(16777215, 200))
        self.widget_5.setSizeIncrement(QSize(0, 20))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(147, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_3 = QSpacerItem(147, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.stage1_label = QLabel(self.widget_5)
        self.stage1_label.setObjectName(u"stage1_label")
        sizePolicy13 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.stage1_label.sizePolicy().hasHeightForWidth())
        self.stage1_label.setSizePolicy(sizePolicy13)
        self.stage1_label.setMinimumSize(QSize(0, 20))
        self.stage1_label.setMaximumSize(QSize(16777215, 20))
        self.stage1_label.setSizeIncrement(QSize(0, 20))
        self.stage1_label.setStyleSheet(u"color:gray;")

        self.horizontalLayout_12.addWidget(self.stage1_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stage2_label = QLabel(self.widget_5)
        self.stage2_label.setObjectName(u"stage2_label")
        sizePolicy13.setHeightForWidth(self.stage2_label.sizePolicy().hasHeightForWidth())
        self.stage2_label.setSizePolicy(sizePolicy13)
        self.stage2_label.setStyleSheet(u"color:gray;")

        self.horizontalLayout_12.addWidget(self.stage2_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stage3_label = QLabel(self.widget_5)
        self.stage3_label.setObjectName(u"stage3_label")
        sizePolicy13.setHeightForWidth(self.stage3_label.sizePolicy().hasHeightForWidth())
        self.stage3_label.setSizePolicy(sizePolicy13)
        self.stage3_label.setStyleSheet(u"color:gray;")

        self.horizontalLayout_12.addWidget(self.stage3_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_4 = QSpacerItem(147, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_6 = QSpacerItem(147, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addWidget(self.widget_5)

        self.backtest_stack = QStackedWidget(self.frame_4)
        self.backtest_stack.setObjectName(u"backtest_stack")
        sizePolicy8.setHeightForWidth(self.backtest_stack.sizePolicy().hasHeightForWidth())
        self.backtest_stack.setSizePolicy(sizePolicy8)
        self.choose_model_page = QWidget()
        self.choose_model_page.setObjectName(u"choose_model_page")
        self.horizontalLayout_11 = QHBoxLayout(self.choose_model_page)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.widget_6 = QWidget(self.choose_model_page)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy8.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy8)
        self.widget_6.setMinimumSize(QSize(100, 300))
        self.widget_6.setMaximumSize(QSize(400, 1000))
        self.widget_6.setSizeIncrement(QSize(0, 0))
        self.widget_6.setBaseSize(QSize(200, 1000))
        self.verticalLayout_6 = QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_11 = QWidget(self.widget_6)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_8 = QVBoxLayout(self.widget_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.model_options = QComboBox(self.widget_11)
        self.model_options.setObjectName(u"model_options")

        self.verticalLayout_8.addWidget(self.model_options)

        self.model_show_table = QTableView(self.widget_11)
        self.model_show_table.setObjectName(u"model_show_table")
        self.model_show_table.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"padding: 0;")

        self.verticalLayout_8.addWidget(self.model_show_table)


        self.verticalLayout_6.addWidget(self.widget_11)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy8.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy8)
        self.widget_7.setMinimumSize(QSize(100, 30))
        self.widget_7.setMaximumSize(QSize(1000, 50))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.stage1_to_next = QPushButton(self.widget_7)
        self.stage1_to_next.setObjectName(u"stage1_to_next")
        sizePolicy8.setHeightForWidth(self.stage1_to_next.sizePolicy().hasHeightForWidth())
        self.stage1_to_next.setSizePolicy(sizePolicy8)
        self.stage1_to_next.setMinimumSize(QSize(100, 25))
        self.stage1_to_next.setMaximumSize(QSize(100, 25))
        self.stage1_to_next.setLayoutDirection(Qt.RightToLeft)
        self.stage1_to_next.setStyleSheet(u"QPushButton {\n"
"border-radius: 10%; \n"
"border: 2px solid rgb(154,197,244);\n"
"background-color: white;\n"
"}\n"
"QPushButton::hover {\n"
"background-color: rgb(154,197,244);\n"
"}\n"
"QPushButton::pressed {\n"
"background-color: white;\n"
"color: rgb(154,197,244)\n"
"}")
        self.stage1_to_next.setIcon(icon4)

        self.horizontalLayout_16.addWidget(self.stage1_to_next)


        self.verticalLayout_6.addWidget(self.widget_7)


        self.horizontalLayout_11.addWidget(self.widget_6)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.backtest_stack.addWidget(self.choose_model_page)
        self.load_data_page = QWidget()
        self.load_data_page.setObjectName(u"load_data_page")
        self.horizontalLayout_14 = QHBoxLayout(self.load_data_page)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_8 = QWidget(self.load_data_page)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy2.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy2)
        self.widget_8.setMinimumSize(QSize(100, 300))
        self.widget_8.setMaximumSize(QSize(800, 1000))
        self.widget_8.setSizeIncrement(QSize(0, 0))
        self.widget_8.setBaseSize(QSize(200, 1000))
        self.verticalLayout_7 = QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_12 = QWidget(self.widget_8)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout = QGridLayout(self.widget_12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tick_file_btn = QPushButton(self.widget_12)
        self.tick_file_btn.setObjectName(u"tick_file_btn")
        sizePolicy14 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.tick_file_btn.sizePolicy().hasHeightForWidth())
        self.tick_file_btn.setSizePolicy(sizePolicy14)
        self.tick_file_btn.setMinimumSize(QSize(20, 25))
        self.tick_file_btn.setMaximumSize(QSize(100, 25))

        self.gridLayout.addWidget(self.tick_file_btn, 1, 1, 1, 1)

        self.tick_file = QLineEdit(self.widget_12)
        self.tick_file.setObjectName(u"tick_file")

        self.gridLayout.addWidget(self.tick_file, 1, 0, 1, 1)

        self.widget_10 = QWidget(self.widget_12)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.tick_table = QTableWidget(self.widget_10)
        self.tick_table.setObjectName(u"tick_table")
        self.tick_table.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"padding: 0;")

        self.horizontalLayout_18.addWidget(self.tick_table)


        self.gridLayout.addWidget(self.widget_10, 2, 0, 1, 2)


        self.verticalLayout_7.addWidget(self.widget_12)

        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy8.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy8)
        self.widget_9.setMinimumSize(QSize(100, 30))
        self.widget_9.setMaximumSize(QSize(1000, 50))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.stage2_to_prev = QPushButton(self.widget_9)
        self.stage2_to_prev.setObjectName(u"stage2_to_prev")
        sizePolicy8.setHeightForWidth(self.stage2_to_prev.sizePolicy().hasHeightForWidth())
        self.stage2_to_prev.setSizePolicy(sizePolicy8)
        self.stage2_to_prev.setMinimumSize(QSize(100, 25))
        self.stage2_to_prev.setMaximumSize(QSize(100, 25))
        self.stage2_to_prev.setLayoutDirection(Qt.RightToLeft)
        self.stage2_to_prev.setStyleSheet(u"QPushButton {\n"
"border-radius: 10%; \n"
"border: 2px solid rgb(154,197,244);\n"
"background-color: white;\n"
"}\n"
"QPushButton::hover {\n"
"background-color: rgb(154,197,244);\n"
"}\n"
"QPushButton::pressed {\n"
"background-color: white;\n"
"color: rgb(154,197,244)\n"
"}")

        self.horizontalLayout_17.addWidget(self.stage2_to_prev)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_10)

        self.stage2_to_next = QPushButton(self.widget_9)
        self.stage2_to_next.setObjectName(u"stage2_to_next")
        sizePolicy8.setHeightForWidth(self.stage2_to_next.sizePolicy().hasHeightForWidth())
        self.stage2_to_next.setSizePolicy(sizePolicy8)
        self.stage2_to_next.setMinimumSize(QSize(100, 25))
        self.stage2_to_next.setMaximumSize(QSize(100, 25))
        self.stage2_to_next.setLayoutDirection(Qt.RightToLeft)
        self.stage2_to_next.setStyleSheet(u"QPushButton {\n"
"border-radius: 10%; \n"
"border: 2px solid rgb(154,197,244);\n"
"background-color: white;\n"
"}\n"
"QPushButton::hover {\n"
"background-color: rgb(154,197,244);\n"
"}\n"
"QPushButton::pressed {\n"
"background-color: white;\n"
"color: rgb(154,197,244)\n"
"}")
        self.stage2_to_next.setIcon(icon4)

        self.horizontalLayout_17.addWidget(self.stage2_to_next)


        self.verticalLayout_7.addWidget(self.widget_9)


        self.horizontalLayout_14.addWidget(self.widget_8)

        self.backtest_stack.addWidget(self.load_data_page)
        self.begin_backtest_page = QWidget()
        self.begin_backtest_page.setObjectName(u"begin_backtest_page")
        self.horizontalLayout_15 = QHBoxLayout(self.begin_backtest_page)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_7 = QPushButton(self.begin_backtest_page)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_15.addWidget(self.pushButton_7)

        self.backtest_stack.addWidget(self.begin_backtest_page)

        self.verticalLayout_5.addWidget(self.backtest_stack)


        self.horizontalLayout_13.addWidget(self.frame_4)

        self.body_stacked.addWidget(self.backtest_pg)
        self.setting_pg = QWidget()
        self.setting_pg.setObjectName(u"setting_pg")
        self.pushButton_4 = QPushButton(self.setting_pg)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(100, 160, 75, 24))
        self.body_stacked.addWidget(self.setting_pg)

        self.horizontalLayout_2.addWidget(self.body_stacked)


        self.horizontalLayout.addWidget(self.body_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.body_stacked.setCurrentIndex(1)
        self.backtest_stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.create_btn.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa", None))
        self.backtest_btn.setText(QCoreApplication.translate("MainWindow", u"\u56de\u6d4b", None))
        self.setting_btn.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"home", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6307\u6807", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u6761\u4ef6", None))
        self.add_metric_btn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0  ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Tick\u6570\u636e", None))
        self.toolButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5206\u949fk\u7ebf", None))
        self.toolButton_2.setText("")
        self.toolButton_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7b56\u7565\u7c7b\u578b", None))
        self.kong_radio.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u5355", None))
        self.duo_radio.setText(QCoreApplication.translate("MainWindow", u"\u591a\u5355", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7b56\u7565\u540d\u79f0", None))
        self.submit_btn.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa", None))
        self.create_tips.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u6309\u7167\u8981\u6267\u884c\u7684\u6307\u6807\u987a\u5e8f,\u586b\u5199\u5408\u9002\u7684\u53c2\u6570\u548c\u6761\u4ef6,\u6dfb\u52a0\u5230\u7b56\u7565\u4e2d;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u9009\u62e9k\u7ebf\u5468\u671f,\u9009\u62e9\u7b56\u7565\u7c7b\u578b, \u586b\u5199\u7b56\u7565\u540d\u79f0,\u521b\u5efa\u7b56\u7565"
                        ".</span></p></body></html>", None))
        self.stage1_label.setText(QCoreApplication.translate("MainWindow", u"\u2460\u9009\u62e9\u7b56\u7565\u2014\u2014", None))
        self.stage2_label.setText(QCoreApplication.translate("MainWindow", u"\u2461\u8f7d\u5165\u6570\u636e\u2014\u2014", None))
        self.stage3_label.setText(QCoreApplication.translate("MainWindow", u"\u2462\u56de\u6d4b", None))
        self.stage1_to_next.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u6b65", None))
        self.tick_file_btn.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.stage2_to_prev.setText(QCoreApplication.translate("MainWindow", u"\u56de\u5230\u4e0a\u6b65", None))
        self.stage2_to_next.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u56de\u6d4b", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"setting", None))
    # retranslateUi

