# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_windowXlwprJ.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QMainWindow, QMenuBar, QPushButton,
                               QScrollArea, QSizePolicy, QSpacerItem, QTextEdit,
                               QVBoxLayout, QWidget)
from static import resource_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1247, 685)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* Central widget: Light grey background */\n"
                                         "#input_frame_2 {\n"
                                         "background-color: rgba(161, 163, 163, 82); \n"
                                         "border: none;  \n"
                                         "border-radius: 10px;   \n"
                                         "}\n"
                                         "#input_textEdit_2{\n"
                                         "background-color: rgba(161, 163, 163, 0); \n"
                                         "border: none;  \n"
                                         "border-radius: 10px;   \n"
                                         "}\n"
                                         "\n"
                                         "QFrame {border:none}\n"
                                         "#upper_frame {border: none}\n"
                                         "#lower_frame {border: none}\n"
                                         "#central_widget {\n"
                                         "    background-color: rgb(211, 211, 211); /* Light grey */\n"
                                         "}\n"
                                         "\n"
                                         "/* Side widgets: White background with slightly rounded borders */\n"
                                         "#side_widget_left, #side_widget_right,  #main_widget, #scrollArea_2  {\n"
                                         "    background-color: rgb(255, 255, 255); /* White */\n"
                                         "    border: 2px solid rgb(255, 255, 255);    /* Greenish border */\n"
                                         "    border-radius: 10px;                  /* Slightly rounded corners */\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "#new_chat_btn{\n"
                                         "    border: 2px solid rgb(211, 211, 211);     /* Greenish border */\n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "#side_widget_left, #side_widget_right,  #"
                                         "main_widget, #scrollArea_2  {\n"
                                         "    padding: 10px;\n"
                                         "}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.upper_frame = QFrame(self.centralwidget)
        self.upper_frame.setObjectName(u"upper_frame")
        self.upper_frame.setMinimumSize(QSize(911, 71))
        self.upper_frame.setMaximumSize(QSize(16777215, 71))
        self.upper_frame.setStyleSheet(u"QPushButton {\n"
                                       "    border: none;\n"
                                       "    padding: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: #f0f0f0;\n"
                                       "}")
        self.upper_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.upper_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.upper_frame.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.upper_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_4 = QPushButton(self.upper_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(75, 0))

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.upper_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.upper_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(678, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.upper_frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 4, 1, 1)

        self.pushButton_7 = QPushButton(self.upper_frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.pushButton_7, 0, 5, 1, 1)

        self.verticalLayout.addWidget(self.upper_frame)

        self.lower_frame = QFrame(self.centralwidget)
        self.lower_frame.setObjectName(u"lower_frame")
        self.lower_frame.setMinimumSize(QSize(0, 577))
        self.lower_frame.setStyleSheet(u"")
        self.lower_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.lower_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.lower_frame)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.main_widget = QWidget(self.lower_frame)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.main_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.input_frame_2 = QFrame(self.main_widget)
        self.input_frame_2.setObjectName(u"input_frame_2")
        self.input_frame_2.setMinimumSize(QSize(650, 0))
        self.input_frame_2.setMaximumSize(QSize(16777215, 200))
        self.input_frame_2.setStyleSheet(u"padding: 10px;")
        self.input_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.input_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.input_frame_2)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(10, 10, 5, 10)
        self.input_textEdit_2 = QTextEdit(self.input_frame_2)
        self.input_textEdit_2.setObjectName(u"input_textEdit_2")
        font = QFont()
        font.setPointSize(10)
        self.input_textEdit_2.setFont(font)
        self.input_textEdit_2.setStyleSheet(u"border: none;")

        self.gridLayout_8.addWidget(self.input_textEdit_2, 0, 0, 2, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.send_btn_2 = QPushButton(self.input_frame_2)
        self.send_btn_2.setObjectName(u"send_btn_2")
        self.send_btn_2.setMinimumSize(QSize(25, 25))
        self.send_btn_2.setMaximumSize(QSize(25, 25))
        self.send_btn_2.setStyleSheet(u"#send_btn {\n"
                                      "border: none;\n"
                                      "padding: 5px;\n"
                                      "border-radius: 5px;\n"
                                      "background:transparent;\n"
                                      "}\n"
                                      "\n"
                                      "#send_btn:hover {\n"
                                      "	background: #ececf1;\n"
                                      "}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/send.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.send_btn_2.setIcon(icon)
        self.send_btn_2.setIconSize(QSize(16, 16))
        self.send_btn_2.setCheckable(False)

        self.gridLayout_8.addWidget(self.send_btn_2, 1, 1, 1, 1)

        self.gridLayout.addWidget(self.input_frame_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 5, 2, 1, 1)

        self.scrollArea_2 = QScrollArea(self.main_widget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"border: none;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 646, 281))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_3.setStyleSheet(u"background-color: rgb(255, 215, 238);")
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setVerticalSpacing(50)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout.addWidget(self.scrollArea_2, 0, 1, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.main_widget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)

        self.horizontalLayout_13.addWidget(self.main_widget)

        self.side_widget_left = QWidget(self.lower_frame)
        self.side_widget_left.setObjectName(u"side_widget_left")
        self.side_widget_left.setMinimumSize(QSize(400, 0))
        self.side_widget_left.setMaximumSize(QSize(250, 16777215))
        self.side_widget_left.setStyleSheet(u"")
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
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_8 = QFrame(self.side_widget_left)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 100))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)

        self.open_alex_btn = QPushButton(self.frame_8)
        self.open_alex_btn.setObjectName(u"open_alex_btn")

        self.gridLayout_4.addWidget(self.open_alex_btn, 4, 0, 1, 1)

        self.archive_btn = QPushButton(self.frame_8)
        self.archive_btn.setObjectName(u"archive_btn")

        self.gridLayout_4.addWidget(self.archive_btn, 5, 0, 1, 1)

        self.upload_pdf_btn = QPushButton(self.frame_8)
        self.upload_pdf_btn.setObjectName(u"upload_pdf_btn")

        self.gridLayout_4.addWidget(self.upload_pdf_btn, 1, 0, 1, 1)

        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.semantic_scholar_btn = QPushButton(self.frame_8)
        self.semantic_scholar_btn.setObjectName(u"semantic_scholar_btn")

        self.gridLayout_4.addWidget(self.semantic_scholar_btn, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 7, 0, 1, 1)

        self.scrollArea = QScrollArea(self.frame_8)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 376, 154))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 2, 0, 1, 1)

        self.verticalLayout_5.addWidget(self.frame_8)

        self.horizontalLayout_13.addWidget(self.side_widget_left)

        self.verticalLayout.addWidget(self.lower_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1247, 37))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Logo", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Conversations", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.input_textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type a message", None))
        self.send_btn_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save to notes", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sources", None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", u"Select the sources on which you want to rely your query", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"External database", None))
        self.open_alex_btn.setText(QCoreApplication.translate("MainWindow", u"Open Alex", None))
        self.archive_btn.setText(QCoreApplication.translate("MainWindow", u"arXiv", None))
        self.upload_pdf_btn.setText(QCoreApplication.translate("MainWindow", u"Upload pdf", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Internal files", None))
        self.semantic_scholar_btn.setText(QCoreApplication.translate("MainWindow", u"Semantic Scholar", None))
    # retranslateUi
