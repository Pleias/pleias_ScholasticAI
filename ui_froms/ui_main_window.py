# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowDjAADV.ui'
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
from static import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1021, 845)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.upper_frame = QFrame(self.centralwidget)
        self.upper_frame.setObjectName(u"upper_frame")
        self.upper_frame.setMinimumSize(QSize(911, 71))
        self.upper_frame.setMaximumSize(QSize(16777215, 71))
        self.upper_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.upper_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.upper_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
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
        self.lower_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.lower_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.lower_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(self.lower_frame)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMinimumSize(QSize(241, 551))
        self.left_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.chut_list_frame = QFrame(self.left_frame)
        self.chut_list_frame.setObjectName(u"chut_list_frame")
        self.chut_list_frame.setGeometry(QRect(13, 97, 221, 561))
        self.chut_list_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.chut_list_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.chat_list = QListView(self.chut_list_frame)
        self.chat_list.setObjectName(u"chat_list")
        self.chat_list.setGeometry(QRect(10, 80, 161, 261))
        self.label = QLabel(self.chut_list_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 171, 16))
        self.pushButton = QPushButton(self.left_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 20, 191, 41))

        self.horizontalLayout.addWidget(self.left_frame)

        self.main_frame = QFrame(self.lower_frame)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(411, 551))
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.main_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.msg_frame_2 = QFrame(self.main_frame)
        self.msg_frame_2.setObjectName(u"msg_frame_2")
        self.msg_frame_2.setMaximumSize(QSize(16777215, 101))
        self.msg_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.msg_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.msg_frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.send_message_btn = QPushButton(self.msg_frame_2)
        self.send_message_btn.setObjectName(u"send_message_btn")
        self.send_message_btn.setMinimumSize(QSize(16, 16))
        self.send_message_btn.setMaximumSize(QSize(300, 300))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSend))
        self.send_message_btn.setIcon(icon)

        self.gridLayout.addWidget(self.send_message_btn, 1, 1, 1, 1)

        self.message_input = QTextEdit(self.msg_frame_2)
        self.message_input.setObjectName(u"message_input")

        self.gridLayout.addWidget(self.message_input, 0, 0, 2, 1)


        self.gridLayout_3.addWidget(self.msg_frame_2, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.scrollArea = QScrollArea(self.main_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 365, 526))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sroll_spacer = QSpacerItem(178, 379, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.sroll_spacer, 3, 0, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 2)


        self.horizontalLayout.addWidget(self.main_frame)

        self.right_frame = QFrame(self.lower_frame)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMinimumSize(QSize(231, 551))
        self.right_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.right_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.right_frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.right_frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.choose_document = QComboBox(self.right_frame)
        self.choose_document.addItem("")
        self.choose_document.addItem("")
        self.choose_document.addItem("")
        self.choose_document.addItem("")
        self.choose_document.setObjectName(u"choose_document")

        self.gridLayout_4.addWidget(self.choose_document, 2, 0, 1, 1)

        self.label_4 = QLabel(self.right_frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)

        self.selected_document_list = QListView(self.right_frame)
        self.selected_document_list.setObjectName(u"selected_document_list")

        self.gridLayout_4.addWidget(self.selected_document_list, 4, 0, 1, 1)


        self.horizontalLayout.addWidget(self.right_frame)


        self.verticalLayout.addWidget(self.lower_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1021, 37))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Logo", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Conversations", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Conversations", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"new chat", None))
        self.send_message_btn.setText("")
        self.message_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d6d6d6;\">wedfwekf</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"User input , akcnlkwencl. kwefkwe wekmekwlf wkeklwemc qwekcmwq ecl", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sources", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Search in", None))
        self.choose_document.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.choose_document.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.choose_document.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.choose_document.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Found in this documents", None))
    # retranslateUi

