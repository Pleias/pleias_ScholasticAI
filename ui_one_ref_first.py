# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one_ref_firstoaKTgN.ui'
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
    QSizePolicy, QWidget)
import resource_rc

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(852, 347)
        Frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.widget = QWidget(Frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(191, 131, 328, 44))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.webEngineView = QWebEngineView(self.widget)
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

        self.horizontalLayout.addWidget(self.webEngineView)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(24, 24))
        self.label_2.setPixmap(QPixmap(u":/icons/icons/logo_openalex.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Frame", u"<!DOCTYPE html>\n"
"<html lang=\"en\">\n"
"<head>\n"
"    <meta charset=\"UTF-8\">\n"
"    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
"    <title>Aligned Content</title>\n"
"    <style>\n"
"        body {\n"
"            font-family: Arial, sans-serif;\n"
"        }\n"
"        .container {\n"
"            display: flex;\n"
"            flex-direction: column;\n"
"            margin: 10px;\n"
"        }\n"
"        .title-row {\n"
"            display: flex;\n"
"            align-items: center;\n"
"        }\n"
"        .icon {\n"
"            width: 20px;\n"
"            height: 20px;\n"
"            margin-right: 10px;\n"
"        }\n"
"        .title {\n"
"            font-family: \"SF Pro\", sans-serif;\n"
"            font-size: 14px;\n"
"            font-weight: 400;\n"
"            line-height: 22px;\n"
"            letter-spacing: -0.43px;\n"
"            text-align: left;\n"
"            text-underline-position: from-font;\n"
"            text-decoration-skip-ink: no"
                        "ne;\n"
"        }\n"
"        .authors {\n"
"            margin-left: 20px;\n"
"            font-family: \"SF Pro\", sans-serif;\n"
"            font-size: 12px;\n"
"            font-weight: 400;\n"
"            line-height: 14.32px;\n"
"            text-align: left;\n"
"            text-underline-position: from-font;\n"
"            text-decoration-skip-ink: none;\n"
"            color: #828282;\n"
"        }\n"
"    </style>\n"
"</head>\n"
"<body>\n"
"    <div class=\"container\">\n"
"        <div class=\"title-row\">\n"
"            <img src=\"/Users/aapoliakova/PycharmProjects/RAG_app_mozzilla/static/icons/icons8-document-ios-17-outlined-16.png\" alt=\"Icon\" class=\"icon\">\n"
"            <span class=\"title\">Attention is All You Need</span>\n"
"        </div>\n"
"        <div class=\"authors\">Ashish Vaswani, Noam Shazeer et al.</div>\n"
"    </div>\n"
"</body>\n"
"</html>\n"
"", None))
        self.label_2.setText("")
    # retranslateUi

