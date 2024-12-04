# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerxZAXRF.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QHBoxLayout, QLabel


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(382, 49)
        Form.setMinimumSize(QSize(49, 49))
        Form.setMaximumSize(QSize(16777215, 49))

        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(20, 25))
        self.label.setMaximumSize(QSize(20, 25))
        self.label.setPixmap(
            QPixmap("static/icons/icons8-document-ios-17-outlined-50.png")
        )
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.label_2.setMinimumSize(QSize(0, 25))
        self.label_2.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.label_2)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", "TextLabel", None))
