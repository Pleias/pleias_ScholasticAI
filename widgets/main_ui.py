# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'backup0nuTruM.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListView, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import resource_rc
import resource_rc
import resource_rc
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1202, 845)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: #fff;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.upper_frame = QFrame(self.centralwidget)
        self.upper_frame.setObjectName(u"upper_frame")
        self.upper_frame.setMinimumSize(QSize(911, 71))
        self.upper_frame.setMaximumSize(QSize(16777215, 71))
        self.upper_frame.setStyleSheet(u"background-color: rgba(169, 169, 169, 189);")
        self.upper_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.upper_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.upper_frame.setLineWidth(0)
        self.gridLayout_6 = QGridLayout(self.upper_frame)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.upper_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_6.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.upper_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_6.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.upper_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_6.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(678, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)


        self.verticalLayout.addWidget(self.upper_frame)

        self.lower_frame = QFrame(self.centralwidget)
        self.lower_frame.setObjectName(u"lower_frame")
        self.lower_frame.setMinimumSize(QSize(0, 577))
        self.lower_frame.setStyleSheet(u"background: #fff;")
        self.lower_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.lower_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.lower_frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.side_widget_right = QWidget(self.lower_frame)
        self.side_widget_right.setObjectName(u"side_widget_right")
        self.side_widget_right.setMinimumSize(QSize(241, 0))
        self.side_widget_right.setMaximumSize(QSize(250, 16777215))
        self.side_widget_right.setStyleSheet(u"background: #fff;")
        self.frame = QFrame(self.side_widget_right)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 241, 48))
        self.frame.setStyleSheet(u"border-color: rgba(255, 255, 255, 0);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.new_chat_btn = QPushButton(self.frame)
        self.new_chat_btn.setObjectName(u"new_chat_btn")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.new_chat_btn.setFont(font)
        self.new_chat_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/add_google_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.new_chat_btn.setIcon(icon)
        self.new_chat_btn.setIconSize(QSize(18, 18))

        self.verticalLayout_2.addWidget(self.new_chat_btn)

        self.frame_3 = QFrame(self.side_widget_right)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 48, 241, 374))
        self.frame_3.setMinimumSize(QSize(0, 100))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.chat_list = QListView(self.frame_3)
        self.chat_list.setObjectName(u"chat_list")
        font1 = QFont()
        font1.setPointSize(11)
        self.chat_list.setFont(font1)
        self.chat_list.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.chat_list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.chat_list, 0, 0, 1, 1)

        self.menu_frame = QFrame(self.side_widget_right)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setGeometry(QRect(0, 422, 241, 331))
        self.menu_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 5, 9, 5)
        self.frame_7 = QFrame(self.menu_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 0, 9, 0)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16, 16))
        self.label_5.setPixmap(QPixmap(u":/icons/icons/delete.svg"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.pushButton_9 = QPushButton(self.frame_7)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"background: none;")

        self.horizontalLayout_8.addWidget(self.pushButton_9)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.menu_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(17, 17))
        self.label.setPixmap(QPixmap(u":/icons/icons/logout.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label)

        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"background: none;")

        self.horizontalLayout_5.addWidget(self.pushButton_6)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.horizontalLayout_13.addWidget(self.side_widget_right)

        self.main_widget = QWidget(self.lower_frame)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setStyleSheet(u"background: #fff;")
        self.gridLayout_7 = QGridLayout(self.main_widget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setVerticalSpacing(6)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 20)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.input_frame_2 = QFrame(self.main_widget)
        self.input_frame_2.setObjectName(u"input_frame_2")
        self.input_frame_2.setMinimumSize(QSize(650, 0))
        self.input_frame_2.setMaximumSize(QSize(16777215, 200))
        self.input_frame_2.setStyleSheet(u"#input_frame\n"
"{\n"
"	border: 1px solid #e5e5e5;\n"
"	background: #fff;\n"
"	border-radius: 5px;\n"
"}")
        self.input_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.input_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.input_frame_2)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(10, 10, 5, 10)
        self.send_btn_2 = QPushButton(self.input_frame_2)
        self.send_btn_2.setObjectName(u"send_btn_2")
        self.send_btn_2.setMinimumSize(QSize(25, 25))
        self.send_btn_2.setMaximumSize(QSize(25, 25))
        self.send_btn_2.setStyleSheet(u"#send_btn {\n"
"border: none;\n"
"padding: 5px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#send_btn:hover {\n"
"	background: #ececf1;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/send.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.send_btn_2.setIcon(icon1)
        self.send_btn_2.setIconSize(QSize(16, 16))

        self.gridLayout_8.addWidget(self.send_btn_2, 1, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.input_textEdit_2 = QTextEdit(self.input_frame_2)
        self.input_textEdit_2.setObjectName(u"input_textEdit_2")
        font2 = QFont()
        font2.setPointSize(10)
        self.input_textEdit_2.setFont(font2)
        self.input_textEdit_2.setStyleSheet(u"border: none;")

        self.gridLayout_8.addWidget(self.input_textEdit_2, 0, 0, 2, 1)


        self.gridLayout_7.addWidget(self.input_frame_2, 1, 1, 1, 1)

        self.scrollArea_2 = QScrollArea(self.main_widget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"border: none;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 718, 522))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setVerticalSpacing(50)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_7.addWidget(self.scrollArea_2, 0, 0, 1, 3)


        self.horizontalLayout_13.addWidget(self.main_widget)

        self.side_widget_left = QWidget(self.lower_frame)
        self.side_widget_left.setObjectName(u"side_widget_left")
        self.side_widget_left.setMinimumSize(QSize(241, 0))
        self.side_widget_left.setMaximumSize(QSize(250, 16777215))
        self.side_widget_left.setStyleSheet(u"background: #fff;\n"
"border:none\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.side_widget_left)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.side_widget_left)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: none")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_8 = QFrame(self.side_widget_left)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 100))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"border: none")

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.chat_list_2 = QListView(self.frame_8)
        self.chat_list_2.setObjectName(u"chat_list_2")
        self.chat_list_2.setFont(font1)
        self.chat_list_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.chat_list_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.chat_list_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.gridLayout_4.addWidget(self.chat_list_2, 4, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.frame_8)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font1)
        self.comboBox_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.comboBox_2.setStyleSheet(u"#comboBox QListView {\n"
"	padding-top:5px;\n"
"	font-size: 11px;\n"
"	background-color: #2a2b32;\n"
"	outline: 0px;  /*\u53bb\u865a\u7ebf*/\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"#comboBox QListView::item{\n"
"	padding-left:5px;\n"
"	background: transparent;\n"
"	padding:5px;\n"
"	color: #fff;\n"
"}\n"
"#comboBox QListView::item:hover{\n"
"   background-color:#1e90ff;\n"
"}\n"
"\n"
"#comboBox QListView::item:selected{\n"
"   background-color:#1e90ff;\n"
"}")

        self.gridLayout_4.addWidget(self.comboBox_2, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.horizontalLayout_13.addWidget(self.side_widget_left)


        self.verticalLayout.addWidget(self.lower_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1202, 24))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Logo", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Conversations", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.new_chat_btn.setText(QCoreApplication.translate("MainWindow", u"New Chat", None))
        self.label_5.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Clear conversations", None))
        self.label.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.send_btn_2.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sources", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Found in this documents:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Search in:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"023487238.pdf ", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"test1.pdf", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"some_other.pdf", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u".......", None))

    # retranslateUi

