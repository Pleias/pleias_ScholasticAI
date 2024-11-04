# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uploaded_docs_widgetndnCMd.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_user_prompts(object):
    def setupUi(self, user_prompts):
        if not user_prompts.objectName():
            user_prompts.setObjectName(u"user_prompts")
        user_prompts.resize(569, 400)
        user_prompts.setMaximumSize(QSize(650, 400))
        user_prompts.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        user_prompts.setStyleSheet(u"\n"
"#user_prompts QPushButton {\n"
"                height: 64px;\n"
"                border-radius: 8px;\n"
"                font-family: \"San Francisco\", sans-serif;\n"
"                font-size: 14px;\n"
"                border: 1px solid #BDBDBD;\n"
"\n"
"                }\n"
"\n"
"                #user_prompts QPushButton:hover {\n"
"                background-color: #F2F2F2;\n"
"\n"
"                }\n"
"\n"
"                QLabel[class=\"placeholder\"] {\n"
"                color: #828282;\n"
"                font-weight: 400;\n"
"                text-align: center;\n"
"                }\n"
"")
        self.gridLayout = QGridLayout(user_prompts)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(user_prompts)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)

        self.gridLayout.addWidget(self.frame, 0, 0, 7, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.frame_2 = QFrame(user_prompts)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)

        self.gridLayout.addWidget(self.frame_2, 0, 2, 7, 1)

        self.label_5 = QLabel(user_prompts)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.pushButton_4 = QPushButton(user_prompts)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(16777215, 45))

        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)

        self.pushButton_3 = QPushButton(user_prompts)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(16777215, 45))

        self.gridLayout.addWidget(self.pushButton_3, 3, 1, 1, 1)

        self.pushButton_2 = QPushButton(user_prompts)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)

        self.pushButton_5 = QPushButton(user_prompts)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.pushButton_5, 5, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 1, 1, 1)


        self.retranslateUi(user_prompts)

        QMetaObject.connectSlotsByName(user_prompts)
    # setupUi

    def retranslateUi(self, user_prompts):
        user_prompts.setWindowTitle(QCoreApplication.translate("user_prompts", u"Frame", None))
        self.label_5.setText(QCoreApplication.translate("user_prompts", u"<html><head/><body><p align=\"center\">Type your\n"
"                            question or choose one of the queries</p></body></html>\n"
"                        ", None))
        self.label_5.setProperty(u"class", QCoreApplication.translate("user_prompts", u"placeholder", None))
        self.pushButton_4.setText(QCoreApplication.translate("user_prompts", u"Create a summary of all uploaded files", None))
        self.pushButton_3.setText(QCoreApplication.translate("user_prompts", u"Why do some people never remember their dreams?", None))
        self.pushButton_2.setText(QCoreApplication.translate("user_prompts", u"Why do some people never remember their dreams?", None))
        self.pushButton_5.setText(QCoreApplication.translate("user_prompts", u"Can we communicate with dreamers while they sleep?", None))
    # retranslateUi

