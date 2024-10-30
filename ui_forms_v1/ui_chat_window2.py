# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_windowCJIowU.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListView, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
from static import resource_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1260, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(
"QLabel {\n"
"    font-family: \"San Francisco\", sans-serif;\n"
"    color: #333;\n"
"    font-size: 14px;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"}\n"
"\n"
"QLabel[class=\"placeholder\"] {\n"
"    color: #828282;\n"
"    font-weight: 400;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QLabel[class=\"subheader\"] {\n"
"    color: #333;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QLabel[class=\"caption\"] {\n"
"    color: #828282;\n"
"    font-size: 12px;\n"
"    font-weight: 400;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 8px;\n"
"    font-family: \"San Francisco\", sans-serif;\n"
"    font-size: 14px;\n"
"    border: 1px solid #BDBDBD;\n"
"    padding: 7px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F2F2F2;\n"
"}\n"
"#msg_input_frame QPushButton {\n"
"    width: 32px;\n"
"    height: 32px;\n"
"    background: #333;\n"
"    padding: 0px;\n"
"    border: none\n"
"}\n"
"#msg_input_frame QPushButton:hover {\n"
"    background: #4F4F4F;\n"
"}\n"
"QLineEdit {\n"
"    font-family: \"San Francisco\", sans-serif;\n"
"    color: #828282;\n"
"    font-size: 14pt;\n"
"    font-weight: 400; \n"
"}\n"
"\n"
"\n"
"/* Central widget: Light grey background */\n"
"#msg_input_frame {\n"
"background-color: #F2F2F2; \n"
"border: none;  \n"
"border-radius: 8px;   \n"
"font-family: \"San Francisco\", sans-serif;\n"
"font-color: #828282;\n"
"font-size: 14px;\n"
"}\n"
"#msg_input_text_edit {\n"
"background-color: rgba(161, 163, 163, 0); \n"
"border: none;  \n"
"border-radius: 8px;   \n"
"}\n"
"\n"
"QFrame {border:none}\n"
"#upper_frame {border: none}\n"
"#conversation_frame {border: none}\n"
"#central_widget {\n"
"    background-color: rgb(211, 211, 211); /* Light grey */\n"
"}\n"
"\n"
"/* Side widgets: White background with slightly rounded borders */\n"
"#side_widget_left, #side_widget_right,  #main_widget, #scrollArea_2  {\n"
"    background-color: rgb(255, 255, 255); /* White */\n"
"    border: 1px solid rgb(255, 255, 255);    /* Greenish border */\n"
"    border-radius: 8px;                  /* Slightly rounded corners */\n"
"}\n"
"\n"
"\n"
"#new_chat_btn{\n"
"    border: 1px solid rgb(211, 211, 211);     /* Greenish border */\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#side_widget_left, #side_widget_right,  #main_widget, #scrollArea_2  {\n"
"    padding: 10px;\n"
"}\n"
"\n"
"")
        self.upper_frame = QFrame(self.centralwidget)
        self.upper_frame.setObjectName(u"upper_frame")
        self.upper_frame.setGeometry(QRect(12, 12, 1236, 71))
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
        self.logo_btn = QPushButton(self.upper_frame)
        self.logo_btn.setObjectName(u"logo_btn")
        self.logo_btn.setMinimumSize(QSize(75, 0))

        self.gridLayout_2.addWidget(self.logo_btn, 0, 0, 1, 1)

        self.library_btn = QPushButton(self.upper_frame)
        self.library_btn.setObjectName(u"library_btn")
        self.library_btn.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.library_btn, 0, 1, 1, 1)

        self.conversation_btn = QPushButton(self.upper_frame)
        self.conversation_btn.setObjectName(u"conversation_btn")
        self.conversation_btn.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.conversation_btn, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(678, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.about_btn = QPushButton(self.upper_frame)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.about_btn, 0, 4, 1, 1)

        self.login_btn = QPushButton(self.upper_frame)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.login_btn, 0, 5, 1, 1)

        self.conversation_frame = QFrame(self.centralwidget)
        self.conversation_frame.setObjectName(u"conversation_frame")
        self.conversation_frame.setGeometry(QRect(12, 99, 1226, 577))
        self.conversation_frame.setMinimumSize(QSize(0, 577))
        self.conversation_frame.setStyleSheet(u"")
        self.conversation_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.conversation_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.conversation_frame)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.main_widget = QWidget(self.conversation_frame)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.main_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.msg_input_frame = QFrame(self.main_widget)
        self.msg_input_frame.setObjectName(u"msg_input_frame")
        self.msg_input_frame.setMinimumSize(QSize(650, 50))
        self.msg_input_frame.setMaximumSize(QSize(16777215, 200))
        self.msg_input_frame.setStyleSheet(u"padding: 10px;")
        self.msg_input_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.msg_input_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.msg_input_frame)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(10, 10, 5, 10)
        self.msg_input_text_edit = QTextEdit(self.msg_input_frame)
        self.msg_input_text_edit.setObjectName(u"msg_input_text_edit")
        self.msg_input_text_edit.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(10)
        self.msg_input_text_edit.setFont(font)
        self.msg_input_text_edit.setStyleSheet(u"border: none;")
        self.msg_input_text_edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)

        self.gridLayout_8.addWidget(self.msg_input_text_edit, 0, 0, 2, 1)

        self.msg_spacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.msg_spacer, 0, 1, 1, 1)

        self.msg_send_btn = QPushButton(self.msg_input_frame)
        self.msg_send_btn.setObjectName(u"msg_send_btn")
        self.msg_send_btn.setMinimumSize(QSize(25, 25))
        self.msg_send_btn.setMaximumSize(QSize(25, 25))
        self.msg_send_btn.setStyleSheet(u"#send_btn {\n"
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
        # icon.addFile(u":/icons/icons/send.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addPixmap(QPixmap("static/icons/icon_arrow_up_white.svg"), QIcon.Normal, QIcon.Off)
        self.msg_send_btn.setIcon(icon)
        self.msg_send_btn.setIconSize(QSize(16, 16))
        self.msg_send_btn.setCheckable(False)

        self.gridLayout_8.addWidget(self.msg_send_btn, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.msg_input_frame, 1, 1, 1, 1)

        self.main_sroll_area = QScrollArea(self.main_widget)
        self.main_sroll_area.setObjectName(u"main_sroll_area")
        self.main_sroll_area.setStyleSheet(u"border: none;")
        self.main_sroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 666, 337))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setVerticalSpacing(50)
        self.label_5 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.label_5, 0, 0, 1, 1)

        self.main_sroll_area.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout.addWidget(self.main_sroll_area, 0, 0, 1, 2)

        self.save_notes_btn = QPushButton(self.main_widget)
        self.save_notes_btn.setObjectName(u"save_notes_btn")

        self.gridLayout.addWidget(self.save_notes_btn, 1, 2, 1, 1)


        self.horizontalLayout_13.addWidget(self.main_widget)

        self.side_widget_left = QWidget(self.conversation_frame)
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
        self.upload_pdf_btn = QPushButton(self.frame_8)
        self.upload_pdf_btn.setObjectName(u"upload_pdf_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.upload_pdf_btn.sizePolicy().hasHeightForWidth())
        self.upload_pdf_btn.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("static/icons/icon_add.svg"), QIcon.Normal, QIcon.Off)
        
        self.upload_pdf_btn.setIcon(icon1)
    
        # Process button
        self.process_btn = QPushButton(self.frame_8)
        self.process_btn.setObjectName(u"process_btn")
        self.process_btn.setSizePolicy(sizePolicy1)
        self.gridLayout_4.addWidget(self.process_btn, 0, 1, 1, 1)  # Add to grid at column 1
    
        self.gridLayout_4.addWidget(self.upload_pdf_btn, 0, 0, 1, 1)

        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)

        self.archive_btn = QPushButton(self.frame_8)
        self.archive_btn.setObjectName(u"archive_btn")

        self.gridLayout_4.addWidget(self.archive_btn, 5, 0, 1, 1)

        self.open_alex_btn = QPushButton(self.frame_8)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("static/icons/logo_openalex.png"), QIcon.Normal, QIcon.Off)
        self.open_alex_btn.setIcon(icon2)
        self.open_alex_btn.setObjectName(u"open_alex_btn")

        self.gridLayout_4.addWidget(self.open_alex_btn, 4, 0, 1, 1)

        self.semantic_scholar_btn = QPushButton(self.frame_8)
        self.semantic_scholar_btn.setObjectName(u"semantic_scholar_btn")

        self.gridLayout_4.addWidget(self.semantic_scholar_btn, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 7, 0, 1, 1)

        self.uploaded_docs_list = QListView(self.frame_8)
        self.uploaded_docs_list.setObjectName(u"uploaded_docs_list")

        self.gridLayout_4.addWidget(self.uploaded_docs_list, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.horizontalLayout_13.addWidget(self.side_widget_left)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1260, 24))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo_btn.setText(_translate("MainWindow", "Logo"))
        self.library_btn.setText(_translate("MainWindow", "Library"))
        self.conversation_btn.setText(_translate("MainWindow", "Conversations"))
        self.about_btn.setText(_translate("MainWindow", "About"))
        self.login_btn.setText(_translate("MainWindow", "Log In"))
        self.msg_input_text_edit.setPlaceholderText(_translate("MainWindow", "Type a message"))
        self.main_sroll_area.setProperty("class", _translate("MainWindow", "subheader"))
        self.label_5.setText(_translate("MainWindow", "Select the sources for your search and start new conversation"))
        self.label_5.setProperty("class", _translate("MainWindow", "placeholder"))
        self.save_notes_btn.setText(_translate("MainWindow", "Save to notes"))
        self.label.setText(_translate("MainWindow", "Local sources"))
        self.label.setProperty("class", _translate("MainWindow", "subheader"))
        self.label_2.setText(_translate("MainWindow", "Add pdf files to be included to your search"))
        self.label_2.setProperty("class", _translate("MainWindow", "caption"))
        self.upload_pdf_btn.setText(_translate("MainWindow", "Add new file"))
        self.label_4.setText(_translate("MainWindow", "Online sources"))
        self.label_4.setProperty("class", _translate("MainWindow", "subheader"))
        self.label_3.setText(_translate("MainWindow", "Include online databases in your search"))
        self.label_3.setProperty("class", _translate("MainWindow", "caption"))
        self.archive_btn.setText(_translate("MainWindow", "arXiv"))
        self.open_alex_btn.setText(_translate("MainWindow", "Enable Open Alex"))
        self.semantic_scholar_btn.setText(_translate("MainWindow", "Semantic Scholar"))
        self.process_btn.setText(_translate("MainWindow", "Process"))
        
    # retranslateUi

