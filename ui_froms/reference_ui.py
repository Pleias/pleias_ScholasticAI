# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerxZAXRF.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(382, 49)
        Form.setMinimumSize(QSize(49, 49))
        Form.setMaximumSize(QSize(16777215, 49))

        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        # Create QLabel for the circle
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFixedSize(25, 25)  # Fixed size for circle
        self.label_3.setStyleSheet("""
            QLabel {
        background-color: rgb(200, 200, 200);  /* Grey background */
        border-radius: 12px;                    /* Circular shape */
        width: 25px;                             /* Width of the label */
        height: 25px;                            /* Height of the label */
        color: white;                            /* Text color */
        font-size: 14px;                         /* Font size */
        text-align: center;                      /* Center text */
        padding: 0px;                           /* No padding for perfect circle */
    }
        """)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setText("1")  # Example number to display

        self.horizontalLayout.addWidget(self.label_3)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(20, 25))
        self.label.setMaximumSize(QSize(20, 25))
        self.label.setPixmap(QPixmap(u"static/icons/icons8-document-ios-17-outlined-50.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))
        self.label_2.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.label_2)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
