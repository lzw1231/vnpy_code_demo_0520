# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1086, 874)
        self.btn_subscribe = QPushButton(Form)
        self.btn_subscribe.setObjectName(u"btn_subscribe")
        self.btn_subscribe.setGeometry(QRect(30, 120, 75, 23))
        self.txt_browser = QTextBrowser(Form)
        self.txt_browser.setObjectName(u"txt_browser")
        self.txt_browser.setGeometry(QRect(130, 10, 941, 851))
        self.txt_symbol = QLineEdit(Form)
        self.txt_symbol.setObjectName(u"txt_symbol")
        self.txt_symbol.setGeometry(QRect(10, 60, 113, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_subscribe.setText(QCoreApplication.translate("Form", u"\u8ba2\u9605", None))
    # retranslateUi

