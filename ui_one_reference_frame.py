# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one_reference_frameUkcfXW.ui'
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


class Ui_one_reference(object):
    def setupUi(self, one_reference):
        if not one_reference.objectName():
            one_reference.setObjectName(u"one_reference")
        one_reference.resize(459, 56)
        self.horizontalLayout = QHBoxLayout(one_reference)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ref_number = QLabel(one_reference)
        self.ref_number.setObjectName(u"ref_number")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_number.sizePolicy().hasHeightForWidth())
        self.ref_number.setSizePolicy(sizePolicy)
        self.ref_number.setMinimumSize(QSize(30, 30))
        self.ref_number.setStyleSheet(u"background-color: rgb(160, 219, 255);\n"
                                      "border-radius:5px;\n"
                                      "color:rgb(108, 109, 109);\n"
                                      "font: 24pt \"Times New Roman\";")
        self.ref_number.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.ref_number)

        self.frame_5 = QFrame(one_reference)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.ref_paper_title.sizePolicy().hasHeightForWidth())
        self.ref_paper_title.setSizePolicy(sizePolicy1)
        self.ref_paper_title.setMinimumSize(QSize(191, 17))

        self.verticalLayout_2.addWidget(self.ref_paper_title)

        self.ref_authors = QLabel(self.frame_7)
        self.ref_authors.setObjectName(u"ref_authors")
        sizePolicy1.setHeightForWidth(self.ref_authors.sizePolicy().hasHeightForWidth())
        self.ref_authors.setSizePolicy(sizePolicy1)
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
        self.ref_text.setMinimumSize(QSize(30, 0))
        self.ref_text.setMaximumSize(QSize(100, 16777215))
        self.ref_text.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.ref_text.setIndent(0)

        self.horizontalLayout_6.addWidget(self.ref_text)

        self.horizontalLayout_5.addWidget(self.frame_8)

        self.horizontalLayout.addWidget(self.frame_5)

        self.retranslateUi(one_reference)

        QMetaObject.connectSlotsByName(one_reference)

    # setupUi

    def retranslateUi(self, one_reference):
        one_reference.setWindowTitle(QCoreApplication.translate("one_reference", u"Frame", None))
        self.ref_number.setText(QCoreApplication.translate("one_reference", u"1", None))
        self.ref_number.setProperty(u"class", QCoreApplication.translate("one_reference", u"reference", None))
        self.ref_start_icon.setText("")
        self.ref_paper_title.setText(QCoreApplication.translate("one_reference", u"Attention is All You Need.", None))
        self.ref_authors.setText(
            QCoreApplication.translate("one_reference", u"2017 Ashish Vaswani, Noam Shazeer et al.", None))
        self.ref_last_icon.setText("")
        self.ref_text.setText(QCoreApplication.translate("one_reference", u"  OpenAlex", None))
    # retranslateUi
