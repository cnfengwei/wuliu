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
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(250, 60, 101, 23))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.comboBox.setFont(font1)
        self.comboBox.setMaxVisibleItems(6)
        self.comboBox.setMaxCount(6)
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 130, 167, 23))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 100, 34, 17))
        self.label_4.setFont(font)
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(250, 120, 231, 131))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 100, 34, 17))
        self.label_2.setFont(font)
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 60, 167, 23))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setSizeIncrement(QSize(11, 19))
        self.lineEdit.setFont(font1)
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setClearButtonEnabled(False)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.textEdit)

        self.retranslateUi(user_edit_window)
        self.buttonBox.accepted.connect(user_edit_window.accept)
        self.buttonBox.rejected.connect(user_edit_window.reject)

        self.comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(user_edit_window)
    # setupUi

    def retranslateUi(self, user_edit_window):
        user_edit_window.setWindowTitle(QCoreApplication.translate("user_edit_window", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("user_edit_window", u"\u7528\u6237\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("user_edit_window", u"\u7528\u6237\u540d", None))
        self.label_3.setText(QCoreApplication.translate("user_edit_window", u"\u6743\u9650", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("user_edit_window", u"0", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("user_edit_window", u"1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("user_edit_window", u"2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("user_edit_window", u"3", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("user_edit_window", u"0", None))
        self.label_4.setText(QCoreApplication.translate("user_edit_window", u"\u5907\u6ce8", None))
        self.label_2.setText(QCoreApplication.translate("user_edit_window", u"\u5bc6\u7801", None))
    # retranslateUi

