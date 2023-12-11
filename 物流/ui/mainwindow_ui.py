# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDateEdit,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1027, 707)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main = QFrame(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Sunken)
        self.gridLayout_2 = QGridLayout(self.main)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_9 = QGridLayout(self.page_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.stackedWidget.addWidget(self.page_4)
        self.page1_bill_serach = QWidget()
        self.page1_bill_serach.setObjectName(u"page1_bill_serach")
        self.gridLayout_7 = QGridLayout(self.page1_bill_serach)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_4 = QLabel(self.page1_bill_serach)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page1_bill_serach)
        self.page2_bill_edit = QWidget()
        self.page2_bill_edit.setObjectName(u"page2_bill_edit")
        self.gridLayout_8 = QGridLayout(self.page2_bill_edit)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tableWidget = QTableWidget(self.page2_bill_edit)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAlternatingRowColors(True)

        self.gridLayout_8.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.page2_bill_edit)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.checkBox_7 = QCheckBox(self.groupBox)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.verticalLayout_2.addWidget(self.checkBox_7)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.dateEdit = QDateEdit(self.groupBox)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMaximumDate(QDate(2050, 1, 1))
        self.dateEdit.setMinimumDate(QDate(2020, 1, 1))
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setDate(QDate(2020, 9, 15))

        self.verticalLayout_2.addWidget(self.dateEdit)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.dateEdit_2 = QDateEdit(self.groupBox)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.verticalLayout_2.addWidget(self.dateEdit_2)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.checkBox_5 = QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_2.addWidget(self.checkBox_5)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.checkBox_6 = QCheckBox(self.groupBox)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_2.addWidget(self.checkBox_6)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.checkBox.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.dateEdit.raise_()
        self.dateEdit_2.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.lineEdit_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.checkBox_5.raise_()
        self.checkBox_6.raise_()
        self.checkBox_7.raise_()
        self.label_6.raise_()
        self.label_5.raise_()

        self.gridLayout_8.addWidget(self.groupBox, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page2_bill_edit)
        self.page3_import_data = QWidget()
        self.page3_import_data.setObjectName(u"page3_import_data")
        self.gridLayout_6 = QGridLayout(self.page3_import_data)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.import_exceldata_btn = QPushButton(self.page3_import_data)
        self.import_exceldata_btn.setObjectName(u"import_exceldata_btn")
        self.import_exceldata_btn.setCheckable(False)

        self.gridLayout_6.addWidget(self.import_exceldata_btn, 1, 0, 1, 1)

        self.save_btn = QPushButton(self.page3_import_data)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setCheckable(True)

        self.gridLayout_6.addWidget(self.save_btn, 1, 1, 1, 1)

        self.table_import_exceldata = QTableWidget(self.page3_import_data)
        if (self.table_import_exceldata.columnCount() < 10):
            self.table_import_exceldata.setColumnCount(10)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(9, __qtablewidgetitem19)
        self.table_import_exceldata.setObjectName(u"table_import_exceldata")
        self.table_import_exceldata.setLineWidth(0)

        self.gridLayout_6.addWidget(self.table_import_exceldata, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.page3_import_data)
        self.page4_users = QWidget()
        self.page4_users.setObjectName(u"page4_users")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(5)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page4_users.sizePolicy().hasHeightForWidth())
        self.page4_users.setSizePolicy(sizePolicy1)
        self.page4_users.setSizeIncrement(QSize(0, 0))
        self.gridLayout_5 = QGridLayout(self.page4_users)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.reload_btn = QPushButton(self.page4_users)
        self.reload_btn.setObjectName(u"reload_btn")

        self.gridLayout_5.addWidget(self.reload_btn, 1, 2, 1, 1)

        self.user_edit_btn = QPushButton(self.page4_users)
        self.user_edit_btn.setObjectName(u"user_edit_btn")
        self.user_edit_btn.setCheckable(False)

        self.gridLayout_5.addWidget(self.user_edit_btn, 1, 1, 1, 1)

        self.add_user_btn = QPushButton(self.page4_users)
        self.add_user_btn.setObjectName(u"add_user_btn")
        self.add_user_btn.setCheckable(False)

        self.gridLayout_5.addWidget(self.add_user_btn, 1, 0, 1, 1)

        self.del_user_btn = QPushButton(self.page4_users)
        self.del_user_btn.setObjectName(u"del_user_btn")
        self.del_user_btn.setMinimumSize(QSize(0, 14))
        self.del_user_btn.setBaseSize(QSize(15, 14))

        self.gridLayout_5.addWidget(self.del_user_btn, 1, 3, 1, 1)

        self.table_users = QTableWidget(self.page4_users)
        if (self.table_users.columnCount() < 5):
            self.table_users.setColumnCount(5)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        self.table_users.setObjectName(u"table_users")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.table_users.sizePolicy().hasHeightForWidth())
        self.table_users.setSizePolicy(sizePolicy2)
        self.table_users.setStyleSheet(u"")
        self.table_users.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_users.setAlternatingRowColors(True)
        self.table_users.verticalHeader().setVisible(False)

        self.gridLayout_5.addWidget(self.table_users, 0, 0, 1, 4)

        self.stackedWidget.addWidget(self.page4_users)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.main, 1, 1, 1, 1)

        self.daohang = QFrame(self.centralwidget)
        self.daohang.setObjectName(u"daohang")
        self.daohang.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.daohang.setFrameShape(QFrame.StyledPanel)
        self.daohang.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.daohang)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.import_data_btn = QPushButton(self.daohang)
        self.import_data_btn.setObjectName(u"import_data_btn")
        self.import_data_btn.setStyleSheet(u"background-color:  rgb(113, 113, 113);\n"
"color:rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icon/icon/notebook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.import_data_btn.setIcon(icon)
        self.import_data_btn.setIconSize(QSize(24, 24))
        self.import_data_btn.setCheckable(True)
        self.import_data_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.import_data_btn)

        self.bill_edit_btn = QPushButton(self.daohang)
        self.bill_edit_btn.setObjectName(u"bill_edit_btn")
        self.bill_edit_btn.setStyleSheet(u"background-color:  rgb(113, 113, 113);\n"
"color:rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/product-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.bill_edit_btn.setIcon(icon1)
        self.bill_edit_btn.setIconSize(QSize(24, 24))
        self.bill_edit_btn.setCheckable(True)
        self.bill_edit_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bill_edit_btn)

        self.bill_serach_btn = QPushButton(self.daohang)
        self.bill_serach_btn.setObjectName(u"bill_serach_btn")
        self.bill_serach_btn.setStyleSheet(u"background-color:  rgb(113, 113, 113);\n"
"color:rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/activity-feed-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.bill_serach_btn.setIcon(icon2)
        self.bill_serach_btn.setIconSize(QSize(24, 24))
        self.bill_serach_btn.setCheckable(True)
        self.bill_serach_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bill_serach_btn)

        self.user_btn = QPushButton(self.daohang)
        self.user_btn.setObjectName(u"user_btn")
        self.user_btn.setStyleSheet(u"background-color:  rgb(113, 113, 113);\n"
"color:rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/group-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon3)
        self.user_btn.setIconSize(QSize(24, 24))
        self.user_btn.setCheckable(True)
        self.user_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.user_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.exit_btn = QPushButton(self.daohang)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/account-logout-64.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon4)
        self.exit_btn.setIconSize(QSize(24, 24))
        self.exit_btn.setCheckable(True)
        self.exit_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.exit_btn)


        self.gridLayout_4.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.daohang)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft YaHei UI\";")
        self.pushButton_8.setInputMethodHints(Qt.ImhNone)
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/huoche.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setIconSize(QSize(32, 32))
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_8, 0, 0, 1, 1)

        self.line = QFrame(self.daohang)
        self.line.setObjectName(u"line")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(29)
        sizePolicy3.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy3)
        self.line.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.daohang, 0, 0, 2, 1)

        self.top = QFrame(self.centralwidget)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(559, 0))
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.top)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_4 = QPushButton(self.top)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background-color: rgb(85, 170, 0);\n"
"font: 12pt \"Microsoft YaHei UI\";")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/arrow-180.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.label = QLabel(self.top)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";")

        self.horizontalLayout.addWidget(self.label)

        self.lcdNumber = QLCDNumber(self.top)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy5)
        self.lcdNumber.setSizeIncrement(QSize(0, 1))
        self.lcdNumber.setStyleSheet(u"color: rgb(114, 255, 250);")
        self.lcdNumber.setFrameShape(QFrame.WinPanel)
        self.lcdNumber.setFrameShadow(QFrame.Plain)
        self.lcdNumber.setLineWidth(4)
        self.lcdNumber.setMidLineWidth(10)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(13)
        self.lcdNumber.setMode(QLCDNumber.Oct)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 5.000000000000000)
        self.lcdNumber.setProperty("intValue", 5)

        self.horizontalLayout.addWidget(self.lcdNumber)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.top, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exit_btn.clicked.connect(MainWindow.close)
        self.user_btn.toggled.connect(MainWindow.on_user_btn_clicked)
        self.import_data_btn.toggled.connect(MainWindow.on_import_data_btn_toggled)
        self.bill_edit_btn.toggled.connect(MainWindow.on_bill_edit_btn_toggled)
        self.bill_serach_btn.toggled.connect(MainWindow.on_bill_serach_btn_toggled)

        self.stackedWidget.setCurrentIndex(2)
        self.pushButton_8.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"billserach", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u8f93\u4efb\u52a1\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6838\u5b9e\u53f8\u673a", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u724c\u53f7", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u91d1\u989d", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u5ba1\u6838", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u4ed8\u6b3e", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65f6\u95f4", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u5355\u53f7", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u53f8\u673a", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u641c\u7d22", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u5355\u53f7", None))
        self.checkBox_7.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u53f8\u673a\u59d3\u540d", None))
        self.checkBox.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65e5\u671f", None))
        self.checkBox_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65e5\u671f", None))
        self.checkBox_3.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u5355\u53f7", None))
        self.checkBox_5.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u724c\u53f7", None))
        self.checkBox_6.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.import_exceldata_btn.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165EXCEL\u6570\u636e", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e", None))
        ___qtablewidgetitem10 = self.table_import_exceldata.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u8fd0\u8f93\u53f7", None));
        ___qtablewidgetitem11 = self.table_import_exceldata.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u5f00\u59cb\u65f6\u95f4", None));
        ___qtablewidgetitem12 = self.table_import_exceldata.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u7ed3\u675f\u65f6\u95f4", None));
        ___qtablewidgetitem13 = self.table_import_exceldata.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u5355\u53f7", None));
        ___qtablewidgetitem14 = self.table_import_exceldata.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u59cb\u53d1\u7f51\u70b9", None));
        ___qtablewidgetitem15 = self.table_import_exceldata.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u7684\u7f51\u70b9", None));
        ___qtablewidgetitem16 = self.table_import_exceldata.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u724c\u53f7", None));
        ___qtablewidgetitem17 = self.table_import_exceldata.horizontalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u8d39\u8f66\u578b", None));
        ___qtablewidgetitem18 = self.table_import_exceldata.horizontalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u53f8\u673a\u59d3\u540d", None));
        ___qtablewidgetitem19 = self.table_import_exceldata.horizontalHeaderItem(9)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u6838\u5b9e\u53f8\u673a", None));
        self.reload_btn.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.user_edit_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.add_user_btn.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e", None))
        self.del_user_btn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        ___qtablewidgetitem20 = self.table_users.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem21 = self.table_users.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None));
        ___qtablewidgetitem22 = self.table_users.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None));
        ___qtablewidgetitem23 = self.table_users.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u6743\u9650", None));
        ___qtablewidgetitem24 = self.table_users.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        self.import_data_btn.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6570\u636e", None))
        self.bill_edit_btn.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u5355\u7f16\u8f91", None))
        self.bill_serach_btn.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u5355\u67e5\u8be2", None))
        self.user_btn.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u7ba1\u7406", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u822a\u680f", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u9500", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237", None))
    # retranslateUi

