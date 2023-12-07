# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_loginwindow(object):
    def setupUi(self, loginwindow):
        if not loginwindow.objectName():
            loginwindow.setObjectName(u"loginwindow")
        loginwindow.resize(466, 243)
        font = QFont()
        font.setPointSize(12)
        loginwindow.setFont(font)
        loginwindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        iconThemeName = u"accessories-dictionary"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        loginwindow.setWindowIcon(icon)
        loginwindow.setLayoutDirection(Qt.LeftToRight)
        loginwindow.setSizeGripEnabled(False)
        loginwindow.setModal(False)
        self.entry_password = QLineEdit(loginwindow)
        self.entry_password.setObjectName(u"entry_password")
        self.entry_password.setGeometry(QRect(160, 120, 181, 31))
        self.entry_user = QLineEdit(loginwindow)
        self.entry_user.setObjectName(u"entry_user")
        self.entry_user.setGeometry(QRect(160, 70, 181, 31))
        self.label = QLabel(loginwindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 70, 81, 31))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(loginwindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 120, 81, 31))
        self.label_2.setFont(font1)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setTextFormat(Qt.RichText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_message = QLabel(loginwindow)
        self.label_message.setObjectName(u"label_message")
        self.label_message.setGeometry(QRect(150, 20, 201, 31))
        font2 = QFont()
        font2.setPointSize(9)
        self.label_message.setFont(font2)
        self.layoutWidget = QWidget(loginwindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(270, 180, 158, 30))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_login = QPushButton(self.layoutWidget)
        self.btn_login.setObjectName(u"btn_login")

        self.horizontalLayout.addWidget(self.btn_login)

        self.btn_quit = QPushButton(self.layoutWidget)
        self.btn_quit.setObjectName(u"btn_quit")

        self.horizontalLayout.addWidget(self.btn_quit)

        QWidget.setTabOrder(self.entry_user, self.entry_password)
        QWidget.setTabOrder(self.entry_password, self.btn_login)
        QWidget.setTabOrder(self.btn_login, self.btn_quit)

        self.retranslateUi(loginwindow)
        self.btn_quit.clicked.connect(loginwindow.close)
        self.entry_user.editingFinished.connect(self.entry_password.setFocus)
        self.entry_password.editingFinished.connect(self.btn_login.setFocus)

        QMetaObject.connectSlotsByName(loginwindow)
    # setupUi

    def retranslateUi(self, loginwindow):
        loginwindow.setWindowTitle(QCoreApplication.translate("loginwindow", u"\u767b\u5f55\u7a97\u53e3", None))
        self.label.setText(QCoreApplication.translate("loginwindow", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("loginwindow", u"\u5bc6       \u7801", None))
        self.label_message.setText("")
        self.btn_login.setText(QCoreApplication.translate("loginwindow", u"\u767b\u5f55", None))
        self.btn_quit.setText(QCoreApplication.translate("loginwindow", u"\u53d6\u6d88", None))
    # retranslateUi

