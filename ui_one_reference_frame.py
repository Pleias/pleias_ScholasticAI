# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one_reference_frameAYnqKS.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)
from static import resource_rc


class Ui_one_reference(object):
    def setupUi(self, one_reference):
        if not one_reference.objectName():
            one_reference.setObjectName(u"one_reference")
        one_reference.resize(452, 52)
        one_reference.setMinimumSize(QSize(0, 25))
        one_reference.setLineWidth(0)

        self.horizontalLayout = QHBoxLayout(one_reference)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.ref_number = QWebEngineView(one_reference)
        self.ref_number.setObjectName(u"ref_number")
        self.ref_number.setMinimumSize(QSize(16, 28))
        self.ref_number.setMaximumSize(QSize(16, 32))
        self.horizontalLayout.addWidget(self.ref_number)

        self.frame_6 = QFrame(one_reference)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())

        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(16, 15))
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_6.setLineWidth(0)
        self.frame_6.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 22))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)


        self.ref_start_icon = QLabel(self.frame)
        self.ref_start_icon.setObjectName(u"ref_start_icon")
        self.ref_start_icon.setMinimumSize(QSize(15, 17))
        self.ref_start_icon.setMaximumSize(QSize(15, 17))
        self.ref_start_icon.setLineWidth(0)
        self.ref_start_icon.setPixmap(QPixmap(u"static/icons/icons8-document-ios-17-outlined-50.png"))
        self.ref_start_icon.setScaledContents(True)
        self.ref_start_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ref_start_icon.setIndent(0)
        self.horizontalLayout_2.addWidget(self.ref_start_icon)
        self.ref_paper_title = QLabel(self.frame)
        self.ref_paper_title.setObjectName(u"ref_paper_title")
        self.ref_paper_title.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ref_paper_title.sizePolicy().hasHeightForWidth())
        self.ref_paper_title.setSizePolicy(sizePolicy1)
        self.ref_paper_title.setMinimumSize(QSize(191, 17))
        font = QFont()
        font.setFamilies([u"STIX Two Text"])
        font.setPointSize(14)
        self.ref_paper_title.setFont(font)
        self.horizontalLayout_2.addWidget(self.ref_paper_title)

        self.verticalLayout.addWidget(self.frame)

        self.ref_authors = QLabel(self.frame_6)
        self.ref_authors.setObjectName(u"ref_authors")
        sizePolicy1.setHeightForWidth(self.ref_authors.sizePolicy().hasHeightForWidth())
        self.ref_authors.setSizePolicy(sizePolicy1)
        self.ref_authors.setMinimumSize(QSize(265, 14))
        self.ref_authors.setMaximumSize(QSize(600, 15))
        self.ref_authors.setIndent(50)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.ref_authors.setFont(font1)
        self.ref_authors.setStyleSheet(u"color: rgb(178, 179, 179);\n""font: 10pt \"Arial\";")
        self.ref_authors.setTextFormat(Qt.TextFormat.RichText)
        self.ref_authors.setWordWrap(True)

        self.ref_authors.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout.addWidget(self.ref_authors)
        self.horizontalLayout.addWidget(self.frame_6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)

        self.frame_8 = QFrame(one_reference)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(101, 40))
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
        self.ref_last_icon.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_6.addWidget(self.ref_last_icon)

        self.ref_text = QLabel(self.frame_8)
        self.ref_text.setObjectName(u"ref_text")
        self.ref_text.setMinimumSize(QSize(69, 40))
        self.ref_text.setMaximumSize(QSize(100, 40))

        font2 = QFont()
        font2.setFamilies([u"Academy Engraved LET"])
        font2.setPointSize(14)
        self.ref_text.setFont(font2)
        self.ref_text.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)
        self.ref_text.setIndent(0)
        self.horizontalLayout_6.addWidget(self.ref_text)
        self.horizontalLayout.addWidget(self.frame_8)
        self.retranslateUi(one_reference)
        QMetaObject.connectSlotsByName(one_reference)
    # setupUi

    def retranslateUi(self, one_reference):
        one_reference.setWindowTitle(QCoreApplication.translate("one_reference", u"Frame", None))
        self.ref_start_icon.setText("")
        self.ref_paper_title.setText(QCoreApplication.translate("one_reference", u"Attention is All You Need.", None))
        self.ref_authors.setText(QCoreApplication.translate("one_reference", u"2017 Ashish Vaswani, Noam Shazeer et al.", None))
        self.ref_last_icon.setText("")
        self.ref_text.setText(QCoreApplication.translate("one_reference", u"  OpenAlex", None))
    # retranslateUi

