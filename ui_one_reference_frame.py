# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one_ref_secondfZfFzE.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QSizePolicy, QSpacerItem,
    QWidget)
from static import resource_rc

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(628, 76)

        self.horizontalLayout = QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.webEngineView = QWebEngineView(Frame)
        self.webEngineView.setObjectName(u"webEngineView")

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy)
        self.webEngineView.setMinimumSize(QSize(31, 31))
        self.webEngineView.setMaximumSize(QSize(31, 31))
        self.webEngineView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.webEngineView.setUrl(QUrl(u"static/square.html"))
        self.horizontalLayout.addWidget(self.webEngineView)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(0)
        self.doc_icon = QLabel(Frame)
        self.doc_icon.setObjectName(u"doc_icon")
        sizePolicy.setHeightForWidth(self.doc_icon.sizePolicy().hasHeightForWidth())
        self.doc_icon.setSizePolicy(sizePolicy)
        self.doc_icon.setMaximumSize(QSize(15, 16))
        self.doc_icon.setTextFormat(Qt.TextFormat.RichText)
        self.doc_icon.setPixmap(QPixmap(u"static/icons/icons8-document-ios-17-outlined-50.png"))
        self.doc_icon.setScaledContents(True)
        self.doc_icon.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.doc_icon.setMargin(0)

        self.gridLayout.addWidget(self.doc_icon, 0, 0, 1, 1)

        self.authors = QLabel(Frame)
        self.authors.setObjectName(u"authors")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.authors.sizePolicy().hasHeightForWidth())
        self.authors.setSizePolicy(sizePolicy1)
        # self.authors.setTextFormat(Qt.TextFormat.RichText)
        self.authors.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.authors.setIndent(0)
        self.authors.setWordWrap(True)
        self.authors.setMinimumWidth(500)
        self.gridLayout.addWidget(self.authors, 1, 1, 1, 1)

        self.titles = QLabel(Frame)
        self.titles.setObjectName(u"titles")
        sizePolicy.setHeightForWidth(self.titles.sizePolicy().hasHeightForWidth())
        self.titles.setSizePolicy(sizePolicy)
        # self.titles.setTextFormat(Qt.TextFormat.RichText)
        self.titles.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.titles.setWordWrap(True)
        self.titles.setIndent(0)
        self.titles.setMinimumWidth(500)

        self.gridLayout.addWidget(self.titles, 0, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(3, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(Frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(24, 24))
        self.label_2.setPixmap(QPixmap(u"static/icons/icons/logo_openalex.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout.addWidget(self.label_2)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.doc_icon.setText("")
        self.authors.setText(QCoreApplication.translate("Frame", u"<html>\n"
"    <head>\n"
"        <style>\n"
"            .authors {\n"
"                margin-left: 20px;\n"
"                font-family: \"SF Pro\", sans-serif;\n"
"                font-size: 12px;\n"
"                font-weight: 400;\n"
"                line-height: 14.32px;\n"
"                text-align: left;\n"
"                text-underline-position: from-font;\n"
"                text-decoration-skip-ink: none;\n"
"                color: #828282;\n"
"            }\n"
"        </style>\n"
"    </head>\n"
"    <body>\n"
"        <span class=\"authors\">Ashish Vaswani, Noam Shazeer et al.</span>\n"
"    </body>\n"
"</html>\n"
"", None))
        self.titles.setText(QCoreApplication.translate("Frame", u"<html>\n"
"    <head>\n"
"        <style>\n"
"            .title {\n"
"                font-family: \"SF Pro\", sans-serif;\n"
"                font-size: 14px;\n"
"                font-weight: 400;\n"
"                line-height: 22px;\n"
"                letter-spacing: -0.43px;\n"
"                text-align: left;\n"
"            }\n"
"        </style>\n"
"    </head>\n"
"    <body>\n"
"        <span class=\"title\">Attention is All You Need</span>\n"
"    </body>\n"
"</html>", None))
        self.label_2.setText("")
    # retranslateUi

