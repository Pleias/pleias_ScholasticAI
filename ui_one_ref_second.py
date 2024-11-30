# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one_ref_seconddVVhPZ.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QSplitter, QWidget)
from static import resource_rc

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.setStyleSheet("border: 2px dashed red;")  # Debug border
        self.splitter = QSplitter(Frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 90, 310, 35))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.webEngineView = QWebEngineView(self.splitter)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy)
        self.webEngineView.setMinimumSize(QSize(31, 31))
        self.webEngineView.setMaximumSize(QSize(31, 31))
        self.webEngineView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.webEngineView.setUrl(QUrl(u"file:///Users/aapoliakova/PycharmProjects/RAG_app_mozzilla/static/square.html"))
        self.splitter.addWidget(self.webEngineView)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.doc_icon = QLabel(self.layoutWidget)
        self.doc_icon.setObjectName(u"doc_icon")
        self.doc_icon.setMaximumSize(QSize(15, 16))
        self.doc_icon.setPixmap(QPixmap(u"static/icons/icons8-document-ios-17-outlined-50.png"))
        self.doc_icon.setScaledContents(True)
        self.doc_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doc_icon.setMargin(0)

        self.gridLayout.addWidget(self.doc_icon, 0, 0, 1, 1)

        self.titles = QLabel(self.layoutWidget)
        self.titles.setObjectName(u"titles")
        self.titles.setTextFormat(Qt.TextFormat.RichText)
        self.titles.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titles.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.titles.setSizePolicy(sizePolicy1)
        self.titles.setMinimumSize(QSize(191, 17))
        self.gridLayout.addWidget(self.titles, 0, 1, 1, 1)

        self.authors = QLabel(self.layoutWidget)
        self.authors.setObjectName(u"authors")
        self.authors.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titles.setSizePolicy(sizePolicy1)
        self.gridLayout.addWidget(self.authors, 1, 1, 1, 1)

        self.splitter.addWidget(self.layoutWidget)
        self.label_2 = QLabel(self.splitter)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(24, 24))
        self.label_2.setPixmap(QPixmap(u"static/icons/icons/logo_openalex.png"))
        self.label_2.setScaledContents(True)
        self.splitter.addWidget(self.label_2)
        self.retranslateUi(Frame)

    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.doc_icon.setText("")
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
        self.label_2.setText("")
    # retranslateUi

