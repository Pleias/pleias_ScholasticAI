# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'documents_listDdfRDK.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from static import resource_rc


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(827, 665)
        Form.setStyleSheet(u"")
        self.references = QFrame(Form)
        self.references.setObjectName(u"references")
        self.references.setGeometry(QRect(10, 20, 801, 382))
        self.references.setStyleSheet(u"#references {\n"
                                      "	background: #FFF;\n"
                                      "	border-radius: 8px;\n"
                                      "	border: none;\n"
                                      "	padding: 10px\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "/* Default style for all QLabel elements */\n"
                                      "QLabel {\n"
                                      "    font-family: \"San Francisco\", sans-serif;\n"
                                      "    color: #333;\n"
                                      "    font-size: 14px;\n"
                                      "    font-style: normal;\n"
                                      "    font-weight: 400;\n"
                                      "    line-height: normal;\n"
                                      "}\n"
                                      "\n"
                                      "QLabel[class=\"subheader\"] {\n"
                                      "    color: #333;\n"
                                      "    font-weight: 700;\n"
                                      "}\n"
                                      "\n"
                                      "QLabel[class=\"reference\"] {\n"
                                      "	color: #042FF4;\n"
                                      "    font-size: 14px;\n"
                                      "    font-weight: 400;\n"
                                      "}\n"
                                      "\n"
                                      "#references QFrame {\n"
                                      "	border: none;\n"
                                      "	padding: 4px 8px;\n"
                                      "}\n"
                                      "\n"
                                      "/* Reference button style */\n"
                                      "#references QPushButton {\n"
                                      "	border-radius: 8px;\n"
                                      "	border: none;\n"
                                      "	font-size: 14px;\n"
                                      "	padding: 7px 12px;\n"
                                      "	text-align: left;\n"
                                      "}\n"
                                      "\n"
                                      "#references QPushButton:hover {\n"
                                      "	background: #F2F2F2;\n"
                                      "}\n"
                                      "")
        self.verticalLayout = QVBoxLayout(self.references)
        # ifndef Q_OS_MAC
        self.verticalLayout.setSpacing(-1)
        # endif
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.ref_frame_3 = QFrame(self.references)
        self.ref_frame_3.setObjectName(u"ref_frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_frame_3.sizePolicy().hasHeightForWidth())
        self.ref_frame_3.setSizePolicy(sizePolicy)
        self.ref_frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.ref_frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.ref_frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.source_frame = QFrame(self.ref_frame_3)
        self.source_frame.setObjectName(u"source_frame")
        self.source_frame.setMinimumSize(QSize(0, 0))
        self.source_frame.setMaximumSize(QSize(16777215, 16777215))
        self.source_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.source_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.source_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.source_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(16, 16))
        self.label_6.setMaximumSize(QSize(64, 16777215))
        self.label_6.setPixmap(QPixmap(u"static/icons/icon_file.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.text = QLabel(self.source_frame)
        self.text.setObjectName(u"text")
        self.text.setMinimumSize(QSize(120, 0))
        self.text.setIndent(0)

        self.horizontalLayout_4.addWidget(self.text)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout_3.addWidget(self.source_frame)

        self.verticalLayout.addWidget(self.ref_frame_3, 0, Qt.AlignTop)

        self.ref_frame_4 = QFrame(self.references)
        self.ref_frame_4.setObjectName(u"ref_frame_4")
        sizePolicy.setHeightForWidth(self.ref_frame_4.sizePolicy().hasHeightForWidth())
        self.ref_frame_4.setSizePolicy(sizePolicy)
        self.ref_frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.ref_frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.ref_frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.source_frame_2 = QFrame(self.ref_frame_4)
        self.source_frame_2.setObjectName(u"source_frame_2")
        self.source_frame_2.setMinimumSize(QSize(0, 0))
        self.source_frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.source_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.source_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.source_frame_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.source_frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(16, 16))
        self.label_7.setMaximumSize(QSize(64, 16777215))
        self.label_7.setPixmap(QPixmap(u"static/icons/icon_file.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.text_2 = QLabel(self.source_frame_2)
        self.text_2.setObjectName(u"text_2")
        self.text_2.setMinimumSize(QSize(120, 0))
        self.text_2.setIndent(0)

        self.horizontalLayout_6.addWidget(self.text_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_5.addWidget(self.source_frame_2)

        self.verticalLayout.addWidget(self.ref_frame_4)

        self.ref_frame_5 = QFrame(self.references)
        self.ref_frame_5.setObjectName(u"ref_frame_5")
        sizePolicy.setHeightForWidth(self.ref_frame_5.sizePolicy().hasHeightForWidth())
        self.ref_frame_5.setSizePolicy(sizePolicy)
        self.ref_frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.ref_frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.ref_frame_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.source_frame_3 = QFrame(self.ref_frame_5)
        self.source_frame_3.setObjectName(u"source_frame_3")
        self.source_frame_3.setMinimumSize(QSize(0, 0))
        self.source_frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.source_frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.source_frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.source_frame_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.source_frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(16, 16))
        self.label_8.setMaximumSize(QSize(64, 16777215))
        self.label_8.setPixmap(QPixmap(u"static/icons/icon_file.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.text_3 = QLabel(self.source_frame_3)
        self.text_3.setObjectName(u"text_3")
        self.text_3.setMinimumSize(QSize(120, 0))
        self.text_3.setIndent(0)

        self.horizontalLayout_8.addWidget(self.text_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_7.addWidget(self.source_frame_3)

        self.verticalLayout.addWidget(self.ref_frame_5)
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText("")
        self.text.setText(QCoreApplication.translate("Form", u"if that is reaaaaaaaaaaaaallly long text", None))
        self.label_7.setText("")
        self.text_2.setText(QCoreApplication.translate("Form", u"FileName.pdf", None))
        self.label_8.setText("")
        self.text_3.setText(QCoreApplication.translate("Form", u"FileName.pdf", None))
    # retranslateUi
