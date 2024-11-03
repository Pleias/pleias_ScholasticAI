# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'referencesTBWNbd.ui'
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
                               QLabel, QSizePolicy, QVBoxLayout, QWidget)
from static import resource_rc


class Ui_reference_from(object):
    def setupUi(self, reference_from):
        if not reference_from.objectName():
            reference_from.setObjectName(u"reference_from")
        reference_from.resize(548, 177)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(reference_from.sizePolicy().hasHeightForWidth())
        reference_from.setSizePolicy(sizePolicy)
        reference_from.setMinimumSize(QSize(30, 30))
        reference_from.setStyleSheet(u"#references {\n"
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
        self.verticalLayout = QVBoxLayout(reference_from)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ref_click_frame = QFrame(reference_from)
        self.ref_click_frame.setObjectName(u"ref_click_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ref_click_frame.sizePolicy().hasHeightForWidth())
        self.ref_click_frame.setSizePolicy(sizePolicy1)
        self.ref_click_frame.setStyleSheet(u"")
        self.ref_click_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.ref_click_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.ref_click_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ref_number = QLabel(self.ref_click_frame)
        self.ref_number.setObjectName(u"ref_number")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ref_number.sizePolicy().hasHeightForWidth())
        self.ref_number.setSizePolicy(sizePolicy2)
        self.ref_number.setMinimumSize(QSize(30, 30))
        self.ref_number.setStyleSheet(u"background-color: rgb(160, 219, 255);\n"
                                      "border-radius:5px;\n"
                                      "color:rgb(108, 109, 109);\n"
                                      "font: 24pt \"Times New Roman\";")
        self.ref_number.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.ref_number)

        self.frame_5 = QFrame(self.ref_click_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy3)
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ref_start_icon = QLabel(self.frame_6)
        self.ref_start_icon.setObjectName(u"ref_start_icon")
        self.ref_start_icon.setMinimumSize(QSize(30, 30))
        self.ref_start_icon.setMaximumSize(QSize(30, 30))
        self.ref_start_icon.setPixmap(QPixmap(u"static/icons/icons8-document-ios-17-outlined-50.png"))
        self.ref_start_icon.setScaledContents(True)
        self.ref_start_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ref_start_icon.setIndent(0)

        self.gridLayout_3.addWidget(self.ref_start_icon, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ref_paper_title = QLabel(self.frame_7)
        self.ref_paper_title.setObjectName(u"ref_paper_title")
        sizePolicy3.setHeightForWidth(self.ref_paper_title.sizePolicy().hasHeightForWidth())
        self.ref_paper_title.setSizePolicy(sizePolicy3)
        self.ref_paper_title.setMinimumSize(QSize(191, 17))

        self.verticalLayout_2.addWidget(self.ref_paper_title)

        self.ref_authors = QLabel(self.frame_7)
        self.ref_authors.setObjectName(u"ref_authors")
        sizePolicy3.setHeightForWidth(self.ref_authors.sizePolicy().hasHeightForWidth())
        self.ref_authors.setSizePolicy(sizePolicy3)
        self.ref_authors.setMaximumSize(QSize(600, 16777215))
        self.ref_authors.setStyleSheet(u"color: rgb(178, 179, 179);\n"
                                       "font: 10pt \"Arial\";")

        self.verticalLayout_2.addWidget(self.ref_authors)

        self.gridLayout_3.addWidget(self.frame_7, 0, 1, 1, 1)

        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 40))
        self.frame_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ref_last_icon = QLabel(self.frame_8)
        self.ref_last_icon.setObjectName(u"ref_last_icon")
        self.ref_last_icon.setMinimumSize(QSize(32, 32))
        self.ref_last_icon.setMaximumSize(QSize(32, 32))
        self.ref_last_icon.setPixmap(QPixmap(u"static/images/logo_openalex.png"))
        self.ref_last_icon.setScaledContents(True)
        self.ref_last_icon.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.ref_last_icon)

        self.ref_text = QLabel(self.frame_8)
        self.ref_text.setObjectName(u"ref_text")
        self.ref_text.setMinimumSize(QSize(120, 0))
        self.ref_text.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)
        self.ref_text.setIndent(0)

        self.horizontalLayout_6.addWidget(self.ref_text)

        self.horizontalLayout_5.addWidget(self.frame_8)

        self.horizontalLayout_4.addWidget(self.frame_5)

        self.verticalLayout.addWidget(self.ref_click_frame)

        self.retranslateUi(reference_from)

        QMetaObject.connectSlotsByName(reference_from)

    # setupUi

    def retranslateUi(self, reference_from):
        reference_from.setWindowTitle(QCoreApplication.translate("reference_from", u"Form", None))
        self.ref_number.setText(QCoreApplication.translate("reference_from", u"1", None))
        self.ref_number.setProperty(u"class", QCoreApplication.translate("reference_from", u"reference", None))
        self.ref_start_icon.setText("")
        self.ref_paper_title.setText(QCoreApplication.translate("reference_from", u"Attention is All You Need.", None))
        self.ref_authors.setText(
            QCoreApplication.translate("reference_from", u"2017 Ashish Vaswani, Noam Shazeer et al.", None))
        self.ref_last_icon.setText("")
        self.ref_text.setText(
            QCoreApplication.translate("reference_from", u"<html><head/><body><p>Open Alex</p></body></html>", None))
    # retranslateUi
