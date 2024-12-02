# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_windowyCtVuQ.ui'
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
        MainWindow.resize(1280, 1094)
        MainWindow.setMinimumSize(QSize(1280, 764))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLabel {\n"
"    font-family: \"San Francisco\", sans-serif;\n"
"    color: #333;\n"
"    font-size: 14px;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"}\n"
"\n"
"QLabel[class=\"placeholder\"] {\n"
"	color: #828282;\n"
"	font-weight: 400;\n"
"	text-align: center;\n"
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
"	border-radius: 8px;\n"
"	font-family: \"San Francisco\", sans-serif;\n"
"	font-size: 14px;\n"
"	border: 1px solid #BDBDBD;\n"
"	padding: 7px 12px;\n"
"}\n"
"\n"
"\n"
"#msg_input_frame QPushButton {\n"
"	width: 32px;\n"
"	height: 32px;\n"
"	background: #333;\n"
"	padding: 0px;\n"
"	border: none\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"	font-family: \"San Francisco\", sans-serif;\n"
"	color: #828282;\n"
"	font-size: 14pt;\n"
"	font-weight: 400; \n"
"}\n"
"\n"
"\n"
"/* Cent"
                        "ral widget: Light grey background */\n"
"#msg_input_frame {\n"
"background-color: rgba(161, 163, 163, 0); \n"
"border: none;  \n"
"border-radius: 8px;   \n"
"}\n"
"\n"
"\n"
"#frame {\n"
"background-color: rgba(161, 163, 163,82); \n"
"border: none;  \n"
"border-top-right-radius: 8px;          /* Rounded corners on the right */\n"
"border-bottom-right-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"#msg_input_text_edit {\n"
"background-color: rgba(161, 163, 163, 82); \n"
"border: none;  \n"
"border-top-left-radius: 8px;          /* Rounded corners on the right */\n"
"border-bottom-left-radius: 8px;\n"
"\n"
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
"#side_widget_left, #side_widget_right,  #main_widget, #main_sroll_area  {\n"
"    background-color: rgb(255, 255, 255); /* White */\n"
"    border: "
                        "1px solid rgb(255, 255, 255);    /* Greenish border */\n"
"    border-radius: 8px;                  /* Slightly rounded corners */\n"
"    padding: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.upper_frame = QFrame(self.centralwidget)
        self.upper_frame.setObjectName(u"upper_frame")
        self.upper_frame.setMinimumSize(QSize(911, 71))
        self.upper_frame.setMaximumSize(QSize(16777215, 64))
        self.upper_frame.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0;\n"
"}")
        self.upper_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.upper_frame.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.upper_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(678, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.library_btn = QPushButton(self.upper_frame)
        self.library_btn.setObjectName(u"library_btn")
        self.library_btn.setMinimumSize(QSize(100, 0))
        self.library_btn.setMaximumSize(QSize(60, 16777215))
        self.library_btn.setStyleSheet(u"QPushButton {\n"
"    font-family: \"SF Pro\";\n"
"    font-size: 18px;\n"
"    font-weight: 510;\n"
"    line-height: 21.48px;\n"
"    text-align: left;\n"
"    text-underline-position: from-font;\n"
"    text-decoration-skip-ink: none;\n"
"    color: #333333;\n"
"    background: transparent; /* Transparent background */\n"
"    border: none; /* Removes borders */\n"
"}\n"
"QPushButton:hover {\n"
"    color: #555555; /* Slightly darker color on hover for feedback */\n"
"}")

        self.gridLayout_2.addWidget(self.library_btn, 0, 1, 1, 1)

        self.login_btn = QPushButton(self.upper_frame)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(100, 0))
        self.login_btn.setStyleSheet(u"QPushButton {\n"
"    font-family: \"SF Pro\";\n"
"    font-size: 18px;\n"
"    font-weight: 510;\n"
"    line-height: 21.48px;\n"
"    text-align: left;\n"
"    text-underline-position: from-font;\n"
"    text-decoration-skip-ink: none;\n"
"    color: #333333;\n"
"    background: transparent; /* Transparent background */\n"
"    border: none; /* Removes borders */\n"
"}\n"
"QPushButton:hover {\n"
"    color: #555555; /* Slightly darker color on hover for feedback */\n"
"}")

        self.gridLayout_2.addWidget(self.login_btn, 0, 5, 1, 1)

        self.conversation_btn = QPushButton(self.upper_frame)
        self.conversation_btn.setObjectName(u"conversation_btn")
        self.conversation_btn.setMinimumSize(QSize(110, 0))
        self.conversation_btn.setStyleSheet(u"QPushButton {\n"
"    font-family: \"SF Pro\";\n"
"    font-size: 18px;\n"
"    font-weight: 510;\n"
"    line-height: 21.48px;\n"
"    text-align: left;\n"
"    text-underline-position: from-font;\n"
"    text-decoration-skip-ink: none;\n"
"    color: #333333;\n"
"    background: transparent; /* Transparent background */\n"
"    border: none; /* Removes borders */\n"
"}\n"
"QPushButton:hover {\n"
"    color: #555555; /* Slightly darker color on hover for feedback */\n"
"}")

        self.gridLayout_2.addWidget(self.conversation_btn, 0, 2, 1, 1)

        self.label_6 = QLabel(self.upper_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 16777215))
        self.label_6.setPixmap(QPixmap(u"static/images/logo_scholastic.svg"))

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.about_btn = QPushButton(self.upper_frame)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setMinimumSize(QSize(100, 0))
        self.about_btn.setStyleSheet(u"QPushButton {\n"
"    font-family: \"SF Pro\";\n"
"    font-size: 18px;\n"
"    font-weight: 510;\n"
"    line-height: 21.48px;\n"
"    text-align: left;\n"
"    text-underline-position: from-font;\n"
"    text-decoration-skip-ink: none;\n"
"    color: #333333;\n"
"    background: transparent; /* Transparent background */\n"
"    border: none; /* Removes borders */\n"
"}\n"
"QPushButton:hover {\n"
"    color: #555555; /* Slightly darker color on hover for feedback */\n"
"}")

        self.gridLayout_2.addWidget(self.about_btn, 0, 4, 1, 1)


        self.verticalLayout_3.addWidget(self.upper_frame)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"QFrame {\n"
"    background-color: #BDBDBD; /* Set the desired color */\n"
"    max-height: 1px; /* For horizontal lines */\n"
"    min-height: 1px;\n"
"    border: none; /* Removes any border */\n"
"}\n"
"")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.new_reaserch_btn = QPushButton(self.centralwidget)
        self.new_reaserch_btn.setObjectName(u"new_reaserch_btn")
        self.new_reaserch_btn.setStyleSheet(u"QPushButton {\n"
"    font-family: \"SF Pro\", sans-serif;\n"
"    font-size: 16px;\n"
"    font-weight: 700;\n"
"    line-height: 19.09px;\n"
"    text-align: left;\n"
"    text-underline-position: from-font;\n"
"    text-decoration-skip-ink: none;\n"
"    border: none; /* Removes borders */\n"
"    background: none; /* Removes background color */\n"
"    padding: 5px 0px 0px 0px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.new_reaserch_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.conversation_frame = QFrame(self.centralwidget)
        self.conversation_frame.setObjectName(u"conversation_frame")
        self.conversation_frame.setMinimumSize(QSize(0, 577))
        self.conversation_frame.setStyleSheet(u"")
        self.conversation_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.conversation_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.main_widget = QWidget(self.conversation_frame)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setMinimumSize(QSize(822, 605))
        self.main_widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.main_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.main_sroll_area = QScrollArea(self.main_widget)
        self.main_sroll_area.setObjectName(u"main_sroll_area")
        self.main_sroll_area.setMaximumSize(QSize(16777215, 16777215))
        self.main_sroll_area.setBaseSize(QSize(5, 0))
        self.main_sroll_area.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 255, 255);")
        self.main_sroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.main_sroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.main_sroll_area.setWidgetResizable(True)
        self.main_sroll_area.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 778, 786))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_3.setStyleSheet(u"background-color: #FFE289;")
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.main_sroll_area.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_2.addWidget(self.main_sroll_area)

        self.frame_3 = QFrame(self.main_widget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setBaseSize(QSize(2, 0))
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.msg_input_frame = QFrame(self.frame_3)
        self.msg_input_frame.setObjectName(u"msg_input_frame")
        self.msg_input_frame.setMinimumSize(QSize(650, 50))
        self.msg_input_frame.setMaximumSize(QSize(16777215, 200))
        self.msg_input_frame.setBaseSize(QSize(0, 45))
        self.msg_input_frame.setStyleSheet(u"")
        self.msg_input_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.msg_input_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.msg_input_text_edit = QTextEdit(self.msg_input_frame)
        self.msg_input_text_edit.setObjectName(u"msg_input_text_edit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.msg_input_text_edit.sizePolicy().hasHeightForWidth())
        self.msg_input_text_edit.setSizePolicy(sizePolicy3)
        self.msg_input_text_edit.setMinimumSize(QSize(600, 32))
        self.msg_input_text_edit.setMaximumSize(QSize(16777215, 200))
        self.msg_input_text_edit.setBaseSize(QSize(600, 45))
        font = QFont()
        font.setPointSize(10)
        self.msg_input_text_edit.setFont(font)
        self.msg_input_text_edit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.msg_input_text_edit.setStyleSheet(u"border: none;")
        self.msg_input_text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.msg_input_text_edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.horizontalLayout.addWidget(self.msg_input_text_edit)

        self.frame = QFrame(self.msg_input_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(32, 32))
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 7, 5)
        self.verticalSpacer = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.msg_send_btn = QPushButton(self.frame)
        self.msg_send_btn.setObjectName(u"msg_send_btn")
        sizePolicy1.setHeightForWidth(self.msg_send_btn.sizePolicy().hasHeightForWidth())
        self.msg_send_btn.setSizePolicy(sizePolicy1)
        self.msg_send_btn.setMinimumSize(QSize(32, 32))
        self.msg_send_btn.setMaximumSize(QSize(32, 32))
        self.msg_send_btn.setStyleSheet(u"#send_btn {\n"
"border: none;\n"
"padding:10px;\n"
"border-radius: 5px;\n"
"background: #333;\n"
"\n"
"}\n"
"\n"
"#send_btn:hover {\n"
"	background: #ececf1;\n"
"}")
        icon = QIcon()
        icon.addFile(u"static/icons/icon_arrow_up_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.msg_send_btn.setIcon(icon)
        self.msg_send_btn.setIconSize(QSize(20, 20))
        self.msg_send_btn.setCheckable(False)

        self.verticalLayout.addWidget(self.msg_send_btn)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_4 = QFrame(self.msg_input_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(32, 32))
        self.frame_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(7, 0, 0, 5)
        self.verticalSpacer_8 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)

        self.save_notes_btn = QPushButton(self.frame_4)
        self.save_notes_btn.setObjectName(u"save_notes_btn")
        sizePolicy1.setHeightForWidth(self.save_notes_btn.sizePolicy().hasHeightForWidth())
        self.save_notes_btn.setSizePolicy(sizePolicy1)
        self.save_notes_btn.setMinimumSize(QSize(100, 32))
        self.save_notes_btn.setMaximumSize(QSize(100, 32))
        self.save_notes_btn.setStyleSheet(u"border-radius: 8px;\n"
"font-family: \"San Francisco\", sans-serif;\n"
"font-size: 14px;\n"
"border: 1px solid #BDBDBD;")

        self.verticalLayout_4.addWidget(self.save_notes_btn)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout_8.addWidget(self.msg_input_frame)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.main_widget)

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
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
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
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.upload_pdf_btn = QPushButton(self.frame_8)
        self.upload_pdf_btn.setObjectName(u"upload_pdf_btn")
        sizePolicy1.setHeightForWidth(self.upload_pdf_btn.sizePolicy().hasHeightForWidth())
        self.upload_pdf_btn.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u"static/icons/icon_add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.upload_pdf_btn.setIcon(icon1)
        self.upload_pdf_btn.setIconSize(QSize(16, 16))

        self.gridLayout_4.addWidget(self.upload_pdf_btn, 0, 0, 1, 1)

        self.archive_btn = QPushButton(self.frame_8)
        self.archive_btn.setObjectName(u"archive_btn")
        icon2 = QIcon()
        icon2.addFile(u"static/icons/archive_2000.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.archive_btn.setIcon(icon2)
        self.archive_btn.setIconSize(QSize(20, 24))

        self.gridLayout_4.addWidget(self.archive_btn, 6, 0, 1, 1)

        self.open_alex_btn = QPushButton(self.frame_8)
        self.open_alex_btn.setObjectName(u"open_alex_btn")
        icon3 = QIcon()
        icon3.addFile(u"static/icons/logo_openalex.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.open_alex_btn.setIcon(icon3)

        self.gridLayout_4.addWidget(self.open_alex_btn, 5, 0, 1, 1)

        self.semantic_scholar_btn = QPushButton(self.frame_8)
        self.semantic_scholar_btn.setObjectName(u"semantic_scholar_btn")
        icon4 = QIcon()
        icon4.addFile(u"static/icons/semantic.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.semantic_scholar_btn.setIcon(icon4)
        self.semantic_scholar_btn.setIconSize(QSize(25, 18))

        self.gridLayout_4.addWidget(self.semantic_scholar_btn, 7, 0, 1, 1)

        self.uploaded_docs_list = QListView(self.frame_8)
        self.uploaded_docs_list.setObjectName(u"uploaded_docs_list")

        self.gridLayout_4.addWidget(self.uploaded_docs_list, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 8, 0, 1, 1)

        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 4, 0, 1, 1)

        self.line = QFrame(self.frame_8)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"QFrame {\n"
"    background-color: #BDBDBD; /* Set the desired color */\n"
"    max-height: 1px; /* For horizontal lines */\n"
"    min-height: 1px;\n"
"    border: none; /* Removes any border */\n"
"}\n"
"")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line, 2, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.side_widget_left)


        self.verticalLayout_3.addWidget(self.conversation_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 24))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.library_btn.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.conversation_btn.setText(QCoreApplication.translate("MainWindow", u"Conversations", None))
        self.label_6.setText("")
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.new_reaserch_btn.setText(QCoreApplication.translate("MainWindow", u"\u2190 new research project", None))
        self.main_sroll_area.setProperty(u"class", QCoreApplication.translate("MainWindow", u"subheader", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Select the sources for your search and start new conversation", None))
        self.label_5.setProperty(u"class", QCoreApplication.translate("MainWindow", u"placeholder", None))
        self.msg_input_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type a message ", None))
        self.msg_send_btn.setText("")
        self.save_notes_btn.setText(QCoreApplication.translate("MainWindow", u"Save to notes", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Local sources", None))
        self.label.setProperty(u"class", QCoreApplication.translate("MainWindow", u"subheader", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Add pdf files to be included to your search", None))
        self.label_2.setProperty(u"class", QCoreApplication.translate("MainWindow", u"caption", None))
        self.upload_pdf_btn.setText(QCoreApplication.translate("MainWindow", u"Add new file", None))
        self.archive_btn.setText(QCoreApplication.translate("MainWindow", u"arXiv", None))
        self.open_alex_btn.setText(QCoreApplication.translate("MainWindow", u"Open Alex", None))
        self.semantic_scholar_btn.setText(QCoreApplication.translate("MainWindow", u"Semantic Scholar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Online sources", None))
        self.label_4.setProperty(u"class", QCoreApplication.translate("MainWindow", u"subheader", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Include online databases in your search", None))
        self.label_3.setProperty(u"class", QCoreApplication.translate("MainWindow", u"caption", None))
    # retranslateUi

