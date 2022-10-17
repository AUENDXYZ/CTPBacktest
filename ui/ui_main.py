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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QComboBox, QDateTimeEdit, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QTimeEdit, QToolButton, QVBoxLayout,
    QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(1159, 550)
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
        self.body_widget.setStyleSheet(u"")
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
        self.verticalLayout_22 = QVBoxLayout(self.home_pg)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_9 = QLabel(self.home_pg)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_9)

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
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(10)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"QGroupBox#groupBox {\n"
"border:none;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.metric_combo = QComboBox(self.groupBox)
        self.metric_combo.setObjectName(u"metric_combo")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.metric_combo.sizePolicy().hasHeightForWidth())
        self.metric_combo.setSizePolicy(sizePolicy5)
        self.metric_combo.setBaseSize(QSize(0, 20))
        font2 = QFont()
        font2.setBold(True)
        self.metric_combo.setFont(font2)
        self.metric_combo.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.metric_combo)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(3)
        sizePolicy6.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy6)
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setStyleSheet(u"QGroupBox#groupBox_2 {\n"
"border:none;\n"
"}")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 18, 0, 0)
        self.scrollArea_2 = QScrollArea(self.groupBox_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setWidgetResizable(True)
        self.params_area = QWidget()
        self.params_area.setObjectName(u"params_area")
        self.params_area.setGeometry(QRect(0, 0, 293, 122))
        self.params_area.setStyleSheet(u"border: 1px solid gray;")
        self.verticalLayout_9 = QVBoxLayout(self.params_area)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.params_layout = QVBoxLayout()
        self.params_layout.setSpacing(0)
        self.params_layout.setObjectName(u"params_layout")
        self.params_layout.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.verticalLayout_9.addLayout(self.params_layout)

        self.scrollArea_2.setWidget(self.params_area)

        self.horizontalLayout_9.addWidget(self.scrollArea_2)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(5)
        sizePolicy7.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy7)
        self.groupBox_3.setFont(font1)
        self.groupBox_3.setStyleSheet(u"QGroupBox#groupBox_3 {\n"
"border:none;\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 18, 0, 0)
        self.scrollArea_3 = QScrollArea(self.groupBox_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"")
        self.scrollArea_3.setWidgetResizable(True)
        self.condition_area = QWidget()
        self.condition_area.setObjectName(u"condition_area")
        self.condition_area.setGeometry(QRect(0, 0, 293, 217))
        self.condition_area.setStyleSheet(u"border: 1px solid gray;")
        self.verticalLayout_10 = QVBoxLayout(self.condition_area)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.condition_layout = QVBoxLayout()
        self.condition_layout.setSpacing(0)
        self.condition_layout.setObjectName(u"condition_layout")

        self.verticalLayout_10.addLayout(self.condition_layout)

        self.scrollArea_3.setWidget(self.condition_area)

        self.horizontalLayout_10.addWidget(self.scrollArea_3)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy8)
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(86, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.add_metric_btn = QPushButton(self.widget)
        self.add_metric_btn.setObjectName(u"add_metric_btn")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.add_metric_btn.sizePolicy().hasHeightForWidth())
        self.add_metric_btn.setSizePolicy(sizePolicy9)
        self.add_metric_btn.setMaximumSize(QSize(100, 50))
        self.add_metric_btn.setFont(font1)
        self.add_metric_btn.setLayoutDirection(Qt.RightToLeft)
        self.add_metric_btn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/create/to_right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_metric_btn.setIcon(icon4)

        self.horizontalLayout_7.addWidget(self.add_metric_btn)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.create_pg)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy10.setHorizontalStretch(1)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy10)
        self.frame_2.setStyleSheet(u"")
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
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_2.setStyleSheet(u"")
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
        self.widget_2.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.kline_spin = QSpinBox(self.widget_2)
        self.kline_spin.setObjectName(u"kline_spin")
        sizePolicy2.setHeightForWidth(self.kline_spin.sizePolicy().hasHeightForWidth())
        self.kline_spin.setSizePolicy(sizePolicy2)
        self.kline_spin.setMaximumSize(QSize(100, 20))
        self.kline_spin.setFont(font1)
        self.kline_spin.setStyleSheet(u"")
        self.kline_spin.setMinimum(1)
        self.kline_spin.setMaximum(1200)
        self.kline_spin.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_4.addWidget(self.kline_spin)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy11 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(2)
        sizePolicy11.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy11)
        self.label.setMaximumSize(QSize(100, 50))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")

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
        sizePolicy12 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(4)
        sizePolicy12.setHeightForWidth(self.widget_aera.sizePolicy().hasHeightForWidth())
        self.widget_aera.setSizePolicy(sizePolicy12)
        self.widget_aera.setMinimumSize(QSize(0, 30))
        self.widget_aera.setMaximumSize(QSize(1000, 1000))
        self.widget_aera.setSizeIncrement(QSize(0, 50))
        self.widget_aera.setStyleSheet(u"")
        self.widget_area = QHBoxLayout(self.widget_aera)
        self.widget_area.setObjectName(u"widget_area")
        self.scrollArea = QScrollArea(self.widget_aera)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContent = QWidget()
        self.scrollAreaContent.setObjectName(u"scrollAreaContent")
        self.scrollAreaContent.setGeometry(QRect(0, 0, 316, 176))
        self.horizontalLayout_19 = QHBoxLayout(self.scrollAreaContent)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.added_layout = QVBoxLayout()
        self.added_layout.setObjectName(u"added_layout")

        self.horizontalLayout_19.addLayout(self.added_layout)

        self.scrollArea.setWidget(self.scrollAreaContent)

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
        self.widget_3.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy11.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy11)
        self.label_2.setMaximumSize(QSize(100, 50))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border: none;")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.kong_radio = QRadioButton(self.widget_3)
        self.kong_radio.setObjectName(u"kong_radio")
        self.kong_radio.setFont(font1)
        self.kong_radio.setStyleSheet(u"border:none;")
        self.kong_radio.setChecked(True)

        self.horizontalLayout_5.addWidget(self.kong_radio)

        self.duo_radio = QRadioButton(self.widget_3)
        self.duo_radio.setObjectName(u"duo_radio")
        self.duo_radio.setFont(font1)
        self.duo_radio.setStyleSheet(u"border: none;")

        self.horizontalLayout_5.addWidget(self.duo_radio)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.frame_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.widget_4.setMaximumSize(QSize(1000, 50))
        self.widget_4.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy11.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy11)
        self.label_3.setMaximumSize(QSize(100, 50))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border: none;")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.model_name = QLineEdit(self.widget_4)
        self.model_name.setObjectName(u"model_name")

        self.horizontalLayout_6.addWidget(self.model_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.submit_btn = QPushButton(self.widget_4)
        self.submit_btn.setObjectName(u"submit_btn")
        sizePolicy9.setHeightForWidth(self.submit_btn.sizePolicy().hasHeightForWidth())
        self.submit_btn.setSizePolicy(sizePolicy9)
        self.submit_btn.setMinimumSize(QSize(60, 0))
        self.submit_btn.setMaximumSize(QSize(100, 50))
        self.submit_btn.setFont(font1)
        self.submit_btn.setStyleSheet(u"")

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
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.create_tips = QTextBrowser(self.frame_3)
        self.create_tips.setObjectName(u"create_tips")
        sizePolicy9.setHeightForWidth(self.create_tips.sizePolicy().hasHeightForWidth())
        self.create_tips.setSizePolicy(sizePolicy9)
        self.create_tips.setStyleSheet(u"")
        self.create_tips.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.create_tips.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

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
        sizePolicy13 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy13)
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
        sizePolicy14 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.stage1_label.sizePolicy().hasHeightForWidth())
        self.stage1_label.setSizePolicy(sizePolicy14)
        self.stage1_label.setMinimumSize(QSize(0, 20))
        self.stage1_label.setMaximumSize(QSize(16777215, 20))
        self.stage1_label.setSizeIncrement(QSize(0, 20))
        self.stage1_label.setStyleSheet(u"color:gray;")

        self.horizontalLayout_12.addWidget(self.stage1_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stage2_label = QLabel(self.widget_5)
        self.stage2_label.setObjectName(u"stage2_label")
        sizePolicy14.setHeightForWidth(self.stage2_label.sizePolicy().hasHeightForWidth())
        self.stage2_label.setSizePolicy(sizePolicy14)
        self.stage2_label.setStyleSheet(u"color:gray;")

        self.horizontalLayout_12.addWidget(self.stage2_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stage3_label = QLabel(self.widget_5)
        self.stage3_label.setObjectName(u"stage3_label")
        sizePolicy14.setHeightForWidth(self.stage3_label.sizePolicy().hasHeightForWidth())
        self.stage3_label.setSizePolicy(sizePolicy14)
        self.stage3_label.setStyleSheet(u"color:gray;")

        self.horizontalLayout_12.addWidget(self.stage3_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_4 = QSpacerItem(147, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_6 = QSpacerItem(147, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addWidget(self.widget_5)

        self.backtest_stack = QStackedWidget(self.frame_4)
        self.backtest_stack.setObjectName(u"backtest_stack")
        sizePolicy9.setHeightForWidth(self.backtest_stack.sizePolicy().hasHeightForWidth())
        self.backtest_stack.setSizePolicy(sizePolicy9)
        self.choose_model_page = QWidget()
        self.choose_model_page.setObjectName(u"choose_model_page")
        self.horizontalLayout_11 = QHBoxLayout(self.choose_model_page)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.widget_6 = QWidget(self.choose_model_page)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy9.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy9)
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
        self.model_options.setFont(font2)
        self.model_options.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.model_options)

        self.model_show = QTextBrowser(self.widget_11)
        self.model_show.setObjectName(u"model_show")
        self.model_show.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.model_show.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.model_show)


        self.verticalLayout_6.addWidget(self.widget_11)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy9.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy9)
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
        sizePolicy9.setHeightForWidth(self.stage1_to_next.sizePolicy().hasHeightForWidth())
        self.stage1_to_next.setSizePolicy(sizePolicy9)
        self.stage1_to_next.setMinimumSize(QSize(100, 25))
        self.stage1_to_next.setMaximumSize(QSize(100, 25))
        self.stage1_to_next.setLayoutDirection(Qt.RightToLeft)
        self.stage1_to_next.setStyleSheet(u"")
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
        sizePolicy15 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy15.setHorizontalStretch(2)
        sizePolicy15.setVerticalStretch(1)
        sizePolicy15.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy15)
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
        sizePolicy5.setHeightForWidth(self.tick_file_btn.sizePolicy().hasHeightForWidth())
        self.tick_file_btn.setSizePolicy(sizePolicy5)
        self.tick_file_btn.setMinimumSize(QSize(20, 25))
        self.tick_file_btn.setMaximumSize(QSize(100, 25))

        self.gridLayout.addWidget(self.tick_file_btn, 1, 1, 1, 1)

        self.tick_file = QLineEdit(self.widget_12)
        self.tick_file.setObjectName(u"tick_file")
        self.tick_file.setStyleSheet(u"")
        self.tick_file.setReadOnly(True)

        self.gridLayout.addWidget(self.tick_file, 1, 0, 1, 1)

        self.widget_10 = QWidget(self.widget_12)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.tick_table = QTableWidget(self.widget_10)
        self.tick_table.setObjectName(u"tick_table")
        self.tick_table.setAutoFillBackground(True)
        self.tick_table.setStyleSheet(u"")
        self.tick_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tick_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tick_table.setAlternatingRowColors(True)
        self.tick_table.setTextElideMode(Qt.ElideLeft)
        self.tick_table.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tick_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tick_table.setSortingEnabled(False)
        self.tick_table.setCornerButtonEnabled(False)
        self.tick_table.horizontalHeader().setCascadingSectionResizes(True)
        self.tick_table.horizontalHeader().setMinimumSectionSize(40)
        self.tick_table.horizontalHeader().setDefaultSectionSize(110)
        self.tick_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.tick_table.horizontalHeader().setStretchLastSection(True)
        self.tick_table.verticalHeader().setMinimumSectionSize(25)
        self.tick_table.verticalHeader().setDefaultSectionSize(32)
        self.tick_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_18.addWidget(self.tick_table)


        self.gridLayout.addWidget(self.widget_10, 2, 0, 1, 2)


        self.verticalLayout_7.addWidget(self.widget_12)

        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy9.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy9)
        self.widget_9.setMinimumSize(QSize(100, 30))
        self.widget_9.setMaximumSize(QSize(1000, 50))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.stage2_to_prev = QPushButton(self.widget_9)
        self.stage2_to_prev.setObjectName(u"stage2_to_prev")
        sizePolicy9.setHeightForWidth(self.stage2_to_prev.sizePolicy().hasHeightForWidth())
        self.stage2_to_prev.setSizePolicy(sizePolicy9)
        self.stage2_to_prev.setMinimumSize(QSize(100, 25))
        self.stage2_to_prev.setMaximumSize(QSize(100, 25))
        self.stage2_to_prev.setLayoutDirection(Qt.RightToLeft)
        self.stage2_to_prev.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.stage2_to_prev)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_10)

        self.stage2_to_next = QPushButton(self.widget_9)
        self.stage2_to_next.setObjectName(u"stage2_to_next")
        sizePolicy9.setHeightForWidth(self.stage2_to_next.sizePolicy().hasHeightForWidth())
        self.stage2_to_next.setSizePolicy(sizePolicy9)
        self.stage2_to_next.setMinimumSize(QSize(100, 25))
        self.stage2_to_next.setMaximumSize(QSize(100, 25))
        self.stage2_to_next.setLayoutDirection(Qt.RightToLeft)
        self.stage2_to_next.setStyleSheet(u"")
        self.stage2_to_next.setIcon(icon4)

        self.horizontalLayout_17.addWidget(self.stage2_to_next)


        self.verticalLayout_7.addWidget(self.widget_9)


        self.horizontalLayout_14.addWidget(self.widget_8)

        self.widget_17 = QWidget(self.load_data_page)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy16 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy16.setHorizontalStretch(1)
        sizePolicy16.setVerticalStretch(1)
        sizePolicy16.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy16)
        self.verticalLayout_14 = QVBoxLayout(self.widget_17)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.groupBox_4 = QGroupBox(self.widget_17)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy17 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(3)
        sizePolicy17.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy17)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 18, -1, -1)
        self.widget_18 = QWidget(self.groupBox_4)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy2.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy2)
        self.horizontalLayout_21 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(6)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.trade_time_add1 = QTimeEdit(self.widget_18)
        self.trade_time_add1.setObjectName(u"trade_time_add1")
        self.trade_time_add1.setCurrentSection(QDateTimeEdit.HourSection)
        self.trade_time_add1.setTime(QTime(21, 0, 0))

        self.horizontalLayout_22.addWidget(self.trade_time_add1)

        self.label_4 = QLabel(self.widget_18)
        self.label_4.setObjectName(u"label_4")
        sizePolicy18 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy18.setHorizontalStretch(0)
        sizePolicy18.setVerticalStretch(0)
        sizePolicy18.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy18)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_4)

        self.trade_time_add2 = QTimeEdit(self.widget_18)
        self.trade_time_add2.setObjectName(u"trade_time_add2")
        self.trade_time_add2.setCurrentSection(QDateTimeEdit.HourSection)
        self.trade_time_add2.setTime(QTime(23, 0, 0))

        self.horizontalLayout_22.addWidget(self.trade_time_add2)

        self.trade_time_add_btn = QPushButton(self.widget_18)
        self.trade_time_add_btn.setObjectName(u"trade_time_add_btn")
        sizePolicy19 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy19.setHorizontalStretch(0)
        sizePolicy19.setVerticalStretch(0)
        sizePolicy19.setHeightForWidth(self.trade_time_add_btn.sizePolicy().hasHeightForWidth())
        self.trade_time_add_btn.setSizePolicy(sizePolicy19)
        self.trade_time_add_btn.setMinimumSize(QSize(20, 18))
        self.trade_time_add_btn.setMaximumSize(QSize(20, 18))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.trade_time_add_btn.setFont(font3)
        self.trade_time_add_btn.setStyleSheet(u"font-weight:bold;\n"
"color: green;")

        self.horizontalLayout_22.addWidget(self.trade_time_add_btn)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_22)


        self.verticalLayout_16.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.groupBox_4)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy12.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy12)
        self.widget_19.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.widget_19)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.scrollArea_4 = QScrollArea(self.widget_19)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 260, 139))
        self.horizontalLayout_23 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.trade_range_layout = QVBoxLayout()
        self.trade_range_layout.setObjectName(u"trade_range_layout")

        self.horizontalLayout_23.addLayout(self.trade_range_layout)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_15.addWidget(self.scrollArea_4)


        self.verticalLayout_16.addWidget(self.widget_19)


        self.verticalLayout_14.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.widget_17)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy11.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy11)
        self.horizontalLayout_31 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, 18, -1, -1)
        self.widget_23 = QWidget(self.groupBox_5)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.widget_23)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_24 = QWidget(self.widget_23)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_10 = QLabel(self.widget_24)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_10)

        self.datetime_col = QComboBox(self.widget_24)
        self.datetime_col.setObjectName(u"datetime_col")

        self.horizontalLayout_32.addWidget(self.datetime_col)


        self.horizontalLayout_35.addLayout(self.horizontalLayout_32)


        self.verticalLayout_17.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.widget_23)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_12 = QLabel(self.widget_25)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_12)

        self.price_col = QComboBox(self.widget_25)
        self.price_col.setObjectName(u"price_col")

        self.horizontalLayout_33.addWidget(self.price_col)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_33)


        self.verticalLayout_17.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.widget_23)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_14 = QLabel(self.widget_26)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_14)

        self.volume_col = QComboBox(self.widget_26)
        self.volume_col.setObjectName(u"volume_col")

        self.horizontalLayout_34.addWidget(self.volume_col)


        self.horizontalLayout_37.addLayout(self.horizontalLayout_34)


        self.verticalLayout_17.addWidget(self.widget_26)


        self.horizontalLayout_31.addWidget(self.widget_23)


        self.verticalLayout_14.addWidget(self.groupBox_5)


        self.horizontalLayout_14.addWidget(self.widget_17)

        self.backtest_stack.addWidget(self.load_data_page)
        self.begin_backtest_page = QWidget()
        self.begin_backtest_page.setObjectName(u"begin_backtest_page")
        self.horizontalLayout_15 = QHBoxLayout(self.begin_backtest_page)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.widget_14 = QWidget(self.begin_backtest_page)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy20 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy20.setHorizontalStretch(6)
        sizePolicy20.setVerticalStretch(0)
        sizePolicy20.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy20)
        self.verticalLayout_11 = QVBoxLayout(self.widget_14)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy21 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy21.setHorizontalStretch(0)
        sizePolicy21.setVerticalStretch(7)
        sizePolicy21.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy21)
        self.verticalLayout_13 = QVBoxLayout(self.widget_15)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.backtest_log = QTextBrowser(self.widget_15)
        self.backtest_log.setObjectName(u"backtest_log")
        self.backtest_log.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.backtest_log)


        self.verticalLayout_11.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.widget_14)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy8.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy8)
        self.horizontalLayout_20 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_11 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_11)

        self.stage3_to_prev = QPushButton(self.widget_16)
        self.stage3_to_prev.setObjectName(u"stage3_to_prev")
        sizePolicy9.setHeightForWidth(self.stage3_to_prev.sizePolicy().hasHeightForWidth())
        self.stage3_to_prev.setSizePolicy(sizePolicy9)
        self.stage3_to_prev.setMinimumSize(QSize(100, 25))
        self.stage3_to_prev.setMaximumSize(QSize(100, 25))
        self.stage3_to_prev.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.stage3_to_prev)

        self.horizontalSpacer_13 = QSpacerItem(12, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_13)

        self.end_backtest_btn = QPushButton(self.widget_16)
        self.end_backtest_btn.setObjectName(u"end_backtest_btn")
        sizePolicy9.setHeightForWidth(self.end_backtest_btn.sizePolicy().hasHeightForWidth())
        self.end_backtest_btn.setSizePolicy(sizePolicy9)
        self.end_backtest_btn.setMinimumSize(QSize(100, 25))
        self.end_backtest_btn.setMaximumSize(QSize(100, 25))
        self.end_backtest_btn.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.end_backtest_btn)

        self.horizontalSpacer_12 = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_12)


        self.verticalLayout_11.addWidget(self.widget_16)


        self.horizontalLayout_15.addWidget(self.widget_14)

        self.widget_28 = QWidget(self.begin_backtest_page)
        self.widget_28.setObjectName(u"widget_28")
        sizePolicy4.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy4)
        self.verticalLayout_21 = QVBoxLayout(self.widget_28)
        self.verticalLayout_21.setSpacing(9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 9, 0, 9)
        self.res_clear_btn = QPushButton(self.widget_28)
        self.res_clear_btn.setObjectName(u"res_clear_btn")
        sizePolicy22 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy22.setHorizontalStretch(0)
        sizePolicy22.setVerticalStretch(0)
        sizePolicy22.setHeightForWidth(self.res_clear_btn.sizePolicy().hasHeightForWidth())
        self.res_clear_btn.setSizePolicy(sizePolicy22)

        self.verticalLayout_21.addWidget(self.res_clear_btn)

        self.res_save_btn = QPushButton(self.widget_28)
        self.res_save_btn.setObjectName(u"res_save_btn")

        self.verticalLayout_21.addWidget(self.res_save_btn)

        self.res_showplot_btn = QPushButton(self.widget_28)
        self.res_showplot_btn.setObjectName(u"res_showplot_btn")

        self.verticalLayout_21.addWidget(self.res_showplot_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_2)


        self.horizontalLayout_15.addWidget(self.widget_28)

        self.backtest_stack.addWidget(self.begin_backtest_page)

        self.verticalLayout_5.addWidget(self.backtest_stack)


        self.horizontalLayout_13.addWidget(self.frame_4)

        self.body_stacked.addWidget(self.backtest_pg)
        self.setting_pg = QWidget()
        self.setting_pg.setObjectName(u"setting_pg")
        self.verticalLayout_18 = QVBoxLayout(self.setting_pg)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_5 = QLabel(self.setting_pg)
        self.label_5.setObjectName(u"label_5")
        sizePolicy8.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy8)

        self.verticalLayout_18.addWidget(self.label_5)

        self.widget_20 = QWidget(self.setting_pg)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy7.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy7)
        self.verticalLayout_19 = QVBoxLayout(self.widget_20)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_22 = QWidget(self.widget_20)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy23 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy23.setHorizontalStretch(0)
        sizePolicy23.setVerticalStretch(0)
        sizePolicy23.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy23)
        self.widget_22.setMinimumSize(QSize(0, 30))
        self.gridLayout_2 = QGridLayout(self.widget_22)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.model_delete_combo = QComboBox(self.widget_22)
        self.model_delete_combo.setObjectName(u"model_delete_combo")
        sizePolicy19.setHeightForWidth(self.model_delete_combo.sizePolicy().hasHeightForWidth())
        self.model_delete_combo.setSizePolicy(sizePolicy19)

        self.gridLayout_2.addWidget(self.model_delete_combo, 0, 2, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_14, 0, 4, 1, 1)

        self.label_7 = QLabel(self.widget_22)
        self.label_7.setObjectName(u"label_7")
        sizePolicy18.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy18)

        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)

        self.model_delete_btn = QPushButton(self.widget_22)
        self.model_delete_btn.setObjectName(u"model_delete_btn")
        sizePolicy19.setHeightForWidth(self.model_delete_btn.sizePolicy().hasHeightForWidth())
        self.model_delete_btn.setSizePolicy(sizePolicy19)
        self.model_delete_btn.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.model_delete_btn, 0, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 2, 2, 1, 1)

        self.label_11 = QLabel(self.widget_22)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 1, 1, 1, 1)

        self.tick_load_rows = QLineEdit(self.widget_22)
        self.tick_load_rows.setObjectName(u"tick_load_rows")
        sizePolicy19.setHeightForWidth(self.tick_load_rows.sizePolicy().hasHeightForWidth())
        self.tick_load_rows.setSizePolicy(sizePolicy19)

        self.gridLayout_2.addWidget(self.tick_load_rows, 1, 2, 1, 1)

        self.tick_load_rows_btn = QPushButton(self.widget_22)
        self.tick_load_rows_btn.setObjectName(u"tick_load_rows_btn")

        self.gridLayout_2.addWidget(self.tick_load_rows_btn, 1, 3, 1, 1)


        self.verticalLayout_19.addWidget(self.widget_22)


        self.verticalLayout_18.addWidget(self.widget_20)

        self.label_6 = QLabel(self.setting_pg)
        self.label_6.setObjectName(u"label_6")
        sizePolicy8.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy8)

        self.verticalLayout_18.addWidget(self.label_6)

        self.widget_21 = QWidget(self.setting_pg)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy7.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy7)
        self.verticalLayout_20 = QVBoxLayout(self.widget_21)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_27 = QWidget(self.widget_21)
        self.widget_27.setObjectName(u"widget_27")
        self.gridLayout_3 = QGridLayout(self.widget_27)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_8 = QLabel(self.widget_27)
        self.label_8.setObjectName(u"label_8")
        sizePolicy18.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy18)

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.dpi_input = QLineEdit(self.widget_27)
        self.dpi_input.setObjectName(u"dpi_input")
        sizePolicy19.setHeightForWidth(self.dpi_input.sizePolicy().hasHeightForWidth())
        self.dpi_input.setSizePolicy(sizePolicy19)

        self.gridLayout_3.addWidget(self.dpi_input, 0, 1, 1, 1)

        self.dpi_save = QPushButton(self.widget_27)
        self.dpi_save.setObjectName(u"dpi_save")
        sizePolicy19.setHeightForWidth(self.dpi_save.sizePolicy().hasHeightForWidth())
        self.dpi_save.setSizePolicy(sizePolicy19)

        self.gridLayout_3.addWidget(self.dpi_save, 0, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_15, 0, 3, 1, 1)


        self.verticalLayout_20.addWidget(self.widget_27)


        self.verticalLayout_18.addWidget(self.widget_21)

        self.widget_29 = QWidget(self.setting_pg)
        self.widget_29.setObjectName(u"widget_29")
        sizePolicy8.setHeightForWidth(self.widget_29.sizePolicy().hasHeightForWidth())
        self.widget_29.setSizePolicy(sizePolicy8)
        self.verticalLayout_23 = QVBoxLayout(self.widget_29)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_about = QLabel(self.widget_29)
        self.label_about.setObjectName(u"label_about")
        font4 = QFont()
        font4.setStyleStrategy(QFont.PreferDefault)
        self.label_about.setFont(font4)
        self.label_about.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_23.addWidget(self.label_about)


        self.verticalLayout_18.addWidget(self.widget_29)

        self.body_stacked.addWidget(self.setting_pg)

        self.horizontalLayout_2.addWidget(self.body_stacked)


        self.horizontalLayout.addWidget(self.body_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.body_stacked.setCurrentIndex(3)
        self.backtest_stack.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CTP\u56de\u6d4b", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.create_btn.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa", None))
        self.backtest_btn.setText(QCoreApplication.translate("MainWindow", u"\u56de\u6d4b", None))
        self.setting_btn.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u8bd5\u7528 CTP\u56de\u6d4b \u5185\u6d4b\u7248", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6307\u6807", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u6761\u4ef6", None))
        self.add_metric_btn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0  ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Tick\u6570\u636e", None))
        self.toolButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5206\u949fk\u7ebf", None))
        self.toolButton_2.setText("")
        self.toolButton_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u5411", None))
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
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613\u65f6\u95f4", None))
        self.trade_time_add1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.trade_time_add2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm", None))
        self.trade_time_add_btn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u5217\u540d", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u5217", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c\u5217", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u6210\u4ea4\u91cf\u5217", None))
        self.stage3_to_prev.setText(QCoreApplication.translate("MainWindow", u"\u56de\u5230\u4e0a\u6b65", None))
        self.end_backtest_btn.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u56de\u6d4b", None))
        self.res_clear_btn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.res_save_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.res_showplot_btn.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u753b\u56fe", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u56de\u6d4b", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u7b56\u7565", None))
        self.model_delete_btn.setText(QCoreApplication.translate("MainWindow", u" \u5220\u9664 ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"tick\u8868\u663e\u793a\u884c\u6570", None))
        self.tick_load_rows_btn.setText(QCoreApplication.translate("MainWindow", u" \u4fdd\u5b58 ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"dpi", None))
        self.dpi_save.setText(QCoreApplication.translate("MainWindow", u" \u4fdd\u5b58 ", None))
        self.label_about.setText("")
    # retranslateUi

