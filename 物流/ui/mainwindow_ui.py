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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
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

        self.bill_sch_btn = QPushButton(self.daohang)
        self.bill_sch_btn.setObjectName(u"bill_sch_btn")
        self.bill_sch_btn.setStyleSheet(u"background-color:  rgb(113, 113, 113);\n"
"color:rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/activity-feed-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.bill_sch_btn.setIcon(icon2)
        self.bill_sch_btn.setIconSize(QSize(24, 24))
        self.bill_sch_btn.setCheckable(True)
        self.bill_sch_btn.setChecked(True)
        self.bill_sch_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bill_sch_btn)

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
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setFlat(True)

        self.gridLayout_4.addWidget(self.pushButton_8, 0, 0, 1, 1)

        self.line = QFrame(self.daohang)
        self.line.setObjectName(u"line")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(29)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";")

        self.horizontalLayout.addWidget(self.label)

        self.lcdNumber = QLCDNumber(self.top)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy2)
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

        self.main = QFrame(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Sunken)
        self.gridLayout_2 = QGridLayout(self.main)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_9 = QGridLayout(self.page_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_5 = QLabel(self.page_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_9.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.bill_serach_page = QWidget()
        self.bill_serach_page.setObjectName(u"bill_serach_page")
        self.gridLayout_7 = QGridLayout(self.bill_serach_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_4 = QLabel(self.bill_serach_page)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.bill_serach_page)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_8 = QGridLayout(self.page_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.bill_edit_page = QLabel(self.page_6)
        self.bill_edit_page.setObjectName(u"bill_edit_page")

        self.gridLayout_8.addWidget(self.bill_edit_page, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_6)
        self.import_data_page = QWidget()
        self.import_data_page.setObjectName(u"import_data_page")
        self.gridLayout_6 = QGridLayout(self.import_data_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableWidget = QTableWidget(self.import_data_page)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
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
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_6.addWidget(self.tableWidget, 0, 0, 1, 2)

        self.import_exceldata_btn = QPushButton(self.import_data_page)
        self.import_exceldata_btn.setObjectName(u"import_exceldata_btn")

        self.gridLayout_6.addWidget(self.import_exceldata_btn, 1, 0, 1, 1)

        self.save_btn = QPushButton(self.import_data_page)
        self.save_btn.setObjectName(u"save_btn")

        self.gridLayout_6.addWidget(self.save_btn, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.import_data_page)
        self.page_users = QWidget()
        self.page_users.setObjectName(u"page_users")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(5)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.page_users.sizePolicy().hasHeightForWidth())
        self.page_users.setSizePolicy(sizePolicy3)
        self.page_users.setSizeIncrement(QSize(0, 10))
        self.gridLayout_5 = QGridLayout(self.page_users)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.table_users = QTableWidget(self.page_users)
        if (self.table_users.columnCount() < 5):
            self.table_users.setColumnCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        self.table_users.setObjectName(u"table_users")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.table_users.sizePolicy().hasHeightForWidth())
        self.table_users.setSizePolicy(sizePolicy4)
        self.table_users.setStyleSheet(u"background-color: rgb(85, 255, 255);")

        self.gridLayout_5.addWidget(self.table_users, 0, 0, 1, 2)

        self.pushButton_10 = QPushButton(self.page_users)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_5.addWidget(self.pushButton_10, 1, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.page_users)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 14))
        self.pushButton_9.setBaseSize(QSize(15, 14))

        self.gridLayout_5.addWidget(self.pushButton_9, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_users)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.main, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exit_btn.clicked.connect(MainWindow.close)
        self.bill_sch_btn.toggled.connect(MainWindow.on_bill_serach_btn_toggled)
        self.user_btn.toggled.connect(MainWindow.on_user_btn_clicked)
        self.import_data_btn.toggled.connect(MainWindow.on_import_data_btn_toggled)
        self.bill_edit_btn.toggled.connect(MainWindow.on_bill_edit_btn_toggled)

        self.pushButton_8.setDefault(True)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.import_data_btn.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6570\u636e", None))
        self.bill_edit_btn.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u5355\u7f16\u8f91", None))
        self.bill_sch_btn.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u5355\u67e5\u8be2", None))
        self.user_btn.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u7ba1\u7406", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u822a\u680f", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u9500", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"importdata", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"billserach", None))
        self.bill_edit_page.setText(QCoreApplication.translate("MainWindow", u"billedit", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u8fd0\u8f93\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        self.import_exceldata_btn.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165EXCEL\u6570\u636e", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e", None))
        ___qtablewidgetitem7 = self.table_users.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem8 = self.table_users.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None));
        ___qtablewidgetitem9 = self.table_users.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None));
        ___qtablewidgetitem10 = self.table_users.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u6743\u9650", None));
        ___qtablewidgetitem11 = self.table_users.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
    # retranslateUi

