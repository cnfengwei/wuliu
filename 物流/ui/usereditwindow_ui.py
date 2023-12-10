# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usereditwindow.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGroupBox, QLabel, QLineEdit,
    QSizePolicy, QTextEdit, QWidget)

class Ui_user_edit_window(object):
    def setupUi(self, user_edit_window):
        if not user_edit_window.objectName():
            user_edit_window.setObjectName(u"user_edit_window")
        user_edit_window.resize(622, 304)
        self.buttonBox = QDialogButtonBox(user_edit_window)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(510, 30, 81, 241))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox = QGroupBox(user_edit_window)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 10, 501, 271))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 51, 17))
        self.label.setFont(font)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 30, 34, 17))
        self.label_3.setFont(font)
        self.qx = QComboBox(self.groupBox)
        self.qx.addItem("")
        self.qx.addItem("")
        self.qx.addItem("")
        self.qx.addItem("")
        self.qx.setObjectName(u"qx")
        self.qx.setGeometry(QRect(250, 60, 101, 23))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.qx.setFont(font1)
        self.qx.setMaxVisibleItems(6)
        self.qx.setMaxCount(6)
        self.password = QLineEdit(self.groupBox)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(20, 130, 167, 23))
        self.password.setFont(font1)
        self.password.setEchoMode(QLineEdit.Normal)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 100, 34, 17))
        self.label_4.setFont(font)
        self.memo = QTextEdit(self.groupBox)
        self.memo.setObjectName(u"memo")
        self.memo.setGeometry(QRect(250, 120, 231, 131))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 100, 34, 17))
        self.label_2.setFont(font)
        self.username = QLineEdit(self.groupBox)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(20, 60, 167, 23))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setSizeIncrement(QSize(11, 19))
        self.username.setFont(font1)
        self.username.setMouseTracking(True)
        self.username.setClearButtonEnabled(False)
        QWidget.setTabOrder(self.username, self.password)
        QWidget.setTabOrder(self.password, self.qx)
        QWidget.setTabOrder(self.qx, self.memo)

        self.retranslateUi(user_edit_window)
        self.buttonBox.accepted.connect(user_edit_window.accept)
        self.buttonBox.rejected.connect(user_edit_window.reject)

        self.qx.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(user_edit_window)
    # setupUi

    def retranslateUi(self, user_edit_window):
        user_edit_window.setWindowTitle(QCoreApplication.translate("user_edit_window", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("user_edit_window", u"\u7528\u6237\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("user_edit_window", u"\u7528\u6237\u540d", None))
        self.label_3.setText(QCoreApplication.translate("user_edit_window", u"\u6743\u9650", None))
        self.qx.setItemText(0, QCoreApplication.translate("user_edit_window", u"0", None))
        self.qx.setItemText(1, QCoreApplication.translate("user_edit_window", u"1", None))
        self.qx.setItemText(2, QCoreApplication.translate("user_edit_window", u"2", None))
        self.qx.setItemText(3, QCoreApplication.translate("user_edit_window", u"3", None))

        self.qx.setCurrentText(QCoreApplication.translate("user_edit_window", u"0", None))
        self.label_4.setText(QCoreApplication.translate("user_edit_window", u"\u5907\u6ce8", None))
        self.label_2.setText(QCoreApplication.translate("user_edit_window", u"\u5bc6\u7801", None))
    # retranslateUi

