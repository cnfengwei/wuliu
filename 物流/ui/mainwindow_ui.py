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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QCheckBox, QDateEdit, QDateTimeEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
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
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
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
        self.table_bill_audits = QTableWidget(self.page1_bill_serach)
        if (self.table_bill_audits.columnCount() < 11):
            self.table_bill_audits.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_bill_audits.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_bill_audits.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_bill_audits.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_bill_audits.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_bill_audits.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_bill_audits.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_bill_audits.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_bill_audits.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_bill_audits.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_bill_audits.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_bill_audits.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.table_bill_audits.setObjectName(u"table_bill_audits")
        self.table_bill_audits.setContextMenuPolicy(Qt.PreventContextMenu)
        self.table_bill_audits.setAcceptDrops(True)
        self.table_bill_audits.setLayoutDirection(Qt.LeftToRight)
        self.table_bill_audits.setAutoFillBackground(True)
        self.table_bill_audits.setStyleSheet(u"")
        self.table_bill_audits.setFrameShadow(QFrame.Raised)
        self.table_bill_audits.setLineWidth(0)
        self.table_bill_audits.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.table_bill_audits.setAutoScroll(True)
        self.table_bill_audits.setAutoScrollMargin(16)
        self.table_bill_audits.setDragEnabled(False)
        self.table_bill_audits.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.table_bill_audits.setDefaultDropAction(Qt.IgnoreAction)
        self.table_bill_audits.setAlternatingRowColors(True)
        self.table_bill_audits.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_bill_audits.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table_bill_audits.setTextElideMode(Qt.ElideRight)
        self.table_bill_audits.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table_bill_audits.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table_bill_audits.setShowGrid(True)
        self.table_bill_audits.setGridStyle(Qt.CustomDashLine)
        self.table_bill_audits.setSortingEnabled(True)
        self.table_bill_audits.setWordWrap(True)
        self.table_bill_audits.setCornerButtonEnabled(True)
        self.table_bill_audits.horizontalHeader().setCascadingSectionResizes(False)
        self.table_bill_audits.horizontalHeader().setMinimumSectionSize(50)
        self.table_bill_audits.horizontalHeader().setDefaultSectionSize(120)
        self.table_bill_audits.horizontalHeader().setHighlightSections(True)
        self.table_bill_audits.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_bill_audits.horizontalHeader().setStretchLastSection(False)
        self.table_bill_audits.verticalHeader().setVisible(True)
        self.table_bill_audits.verticalHeader().setDefaultSectionSize(30)
        self.table_bill_audits.verticalHeader().setProperty("showSortIndicator", False)

        self.gridLayout_7.addWidget(self.table_bill_audits, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.page1_bill_serach)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setCheckable(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.cb_drivename_audits = QCheckBox(self.groupBox_2)
        self.cb_drivename_audits.setObjectName(u"cb_drivename_audits")

        self.verticalLayout_4.addWidget(self.cb_drivename_audits)

        self.drivename__audits = QLineEdit(self.groupBox_2)
        self.drivename__audits.setObjectName(u"drivename__audits")

        self.verticalLayout_4.addWidget(self.drivename__audits)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)

        self.cb_startdate__audits = QCheckBox(self.groupBox_2)
        self.cb_startdate__audits.setObjectName(u"cb_startdate__audits")

        self.verticalLayout_4.addWidget(self.cb_startdate__audits)

        self.startdate__audits = QDateEdit(self.groupBox_2)
        self.startdate__audits.setObjectName(u"startdate__audits")
        self.startdate__audits.setAcceptDrops(False)
        self.startdate__audits.setAccelerated(True)
        self.startdate__audits.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.startdate__audits.setMaximumDate(QDate(2050, 1, 1))
        self.startdate__audits.setMinimumDate(QDate(2020, 8, 1))
        self.startdate__audits.setCurrentSection(QDateTimeEdit.YearSection)
        self.startdate__audits.setCalendarPopup(True)
        self.startdate__audits.setDate(QDate(2023, 8, 1))

        self.verticalLayout_4.addWidget(self.startdate__audits)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.cb_enddate__audits = QCheckBox(self.groupBox_2)
        self.cb_enddate__audits.setObjectName(u"cb_enddate__audits")

        self.verticalLayout_4.addWidget(self.cb_enddate__audits)

        self.enddate__audits = QDateEdit(self.groupBox_2)
        self.enddate__audits.setObjectName(u"enddate__audits")
        self.enddate__audits.setDateTime(QDateTime(QDate(2023, 8, 2), QTime(0, 0, 0)))
        self.enddate__audits.setMinimumDate(QDate(2020, 8, 1))
        self.enddate__audits.setCurrentSection(QDateTimeEdit.YearSection)
        self.enddate__audits.setCalendarPopup(True)
        self.enddate__audits.setTimeSpec(Qt.UTC)

        self.verticalLayout_4.addWidget(self.enddate__audits)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.cb_audits = QCheckBox(self.groupBox_2)
        self.cb_audits.setObjectName(u"cb_audits")
        self.cb_audits.setCheckable(True)
        self.cb_audits.setChecked(False)

        self.verticalLayout_4.addWidget(self.cb_audits)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setStyleSheet(u"color: rgb(255, 32, 91);\n"
"font: 11pt \"Microsoft YaHei UI\";")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_11)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_serach_audits = QPushButton(self.groupBox_2)
        self.btn_serach_audits.setObjectName(u"btn_serach_audits")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_serach_audits.sizePolicy().hasHeightForWidth())
        self.btn_serach_audits.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(12)
        self.btn_serach_audits.setFont(font)

        self.verticalLayout_5.addWidget(self.btn_serach_audits)

        self.btn_bill_update__audits = QPushButton(self.groupBox_2)
        self.btn_bill_update__audits.setObjectName(u"btn_bill_update__audits")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_bill_update__audits.sizePolicy().hasHeightForWidth())
        self.btn_bill_update__audits.setSizePolicy(sizePolicy4)
        self.btn_bill_update__audits.setFont(font)

        self.verticalLayout_5.addWidget(self.btn_bill_update__audits)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)


        self.gridLayout_7.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page1_bill_serach)
        self.page2_bill_edit = QWidget()
        self.page2_bill_edit.setObjectName(u"page2_bill_edit")
        self.gridLayout_8 = QGridLayout(self.page2_bill_edit)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.table_bill_edit = QTableWidget(self.page2_bill_edit)
        if (self.table_bill_edit.columnCount() < 11):
            self.table_bill_edit.setColumnCount(11)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_bill_edit.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_bill_edit.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_bill_edit.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_bill_edit.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_bill_edit.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_bill_edit.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_bill_edit.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_bill_edit.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_bill_edit.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_bill_edit.setHorizontalHeaderItem(9, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_bill_edit.setHorizontalHeaderItem(10, __qtablewidgetitem21)
        self.table_bill_edit.setObjectName(u"table_bill_edit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(200)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.table_bill_edit.sizePolicy().hasHeightForWidth())
        self.table_bill_edit.setSizePolicy(sizePolicy5)
        self.table_bill_edit.setAcceptDrops(True)
        self.table_bill_edit.setAutoScroll(True)
        self.table_bill_edit.setDragEnabled(True)
        self.table_bill_edit.setAlternatingRowColors(True)
        self.table_bill_edit.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_bill_edit.setSortingEnabled(True)
        self.table_bill_edit.setWordWrap(True)
        self.table_bill_edit.setCornerButtonEnabled(True)
        self.table_bill_edit.horizontalHeader().setVisible(True)
        self.table_bill_edit.horizontalHeader().setCascadingSectionResizes(False)
        self.table_bill_edit.horizontalHeader().setDefaultSectionSize(120)
        self.table_bill_edit.horizontalHeader().setHighlightSections(False)
        self.table_bill_edit.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_bill_edit.verticalHeader().setVisible(True)
        self.table_bill_edit.verticalHeader().setProperty("showSortIndicator", True)

        self.gridLayout_8.addWidget(self.table_bill_edit, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.page2_bill_edit)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setCheckable(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.cb_drivename = QCheckBox(self.groupBox)
        self.cb_drivename.setObjectName(u"cb_drivename")

        self.verticalLayout_3.addWidget(self.cb_drivename)

        self.drivename = QLineEdit(self.groupBox)
        self.drivename.setObjectName(u"drivename")

        self.verticalLayout_3.addWidget(self.drivename)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.cb_startdate = QCheckBox(self.groupBox)
        self.cb_startdate.setObjectName(u"cb_startdate")

        self.verticalLayout_3.addWidget(self.cb_startdate)

        self.startdate = QDateEdit(self.groupBox)
        self.startdate.setObjectName(u"startdate")
        self.startdate.setAccelerated(True)
        self.startdate.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.startdate.setMaximumDate(QDate(2050, 1, 1))
        self.startdate.setMinimumDate(QDate(2020, 8, 1))
        self.startdate.setCalendarPopup(True)
        self.startdate.setDate(QDate(2023, 8, 1))

        self.verticalLayout_3.addWidget(self.startdate)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.cb_enddate = QCheckBox(self.groupBox)
        self.cb_enddate.setObjectName(u"cb_enddate")

        self.verticalLayout_3.addWidget(self.cb_enddate)

        self.enddate = QDateEdit(self.groupBox)
        self.enddate.setObjectName(u"enddate")
        self.enddate.setDateTime(QDateTime(QDate(2023, 8, 3), QTime(0, 0, 0)))
        self.enddate.setMinimumDate(QDate(2020, 8, 1))
        self.enddate.setCurrentSection(QDateTimeEdit.YearSection)
        self.enddate.setCalendarPopup(True)
        self.enddate.setTimeSpec(Qt.UTC)

        self.verticalLayout_3.addWidget(self.enddate)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.checkBox_5 = QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_3.addWidget(self.checkBox_5)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)
        self.label_2.setStyleSheet(u"color: rgb(255, 32, 91);\n"
"font: 11pt \"Microsoft YaHei UI\";")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_serach = QPushButton(self.groupBox)
        self.btn_serach.setObjectName(u"btn_serach")
        sizePolicy3.setHeightForWidth(self.btn_serach.sizePolicy().hasHeightForWidth())
        self.btn_serach.setSizePolicy(sizePolicy3)
        self.btn_serach.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_serach)

        self.btn_bill_update = QPushButton(self.groupBox)
        self.btn_bill_update.setObjectName(u"btn_bill_update")
        sizePolicy4.setHeightForWidth(self.btn_bill_update.sizePolicy().hasHeightForWidth())
        self.btn_bill_update.setSizePolicy(sizePolicy4)
        self.btn_bill_update.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_bill_update)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.cb_drivename.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.startdate.raise_()
        self.enddate.raise_()
        self.cb_startdate.raise_()
        self.cb_enddate.raise_()
        self.drivename.raise_()
        self.label_7.raise_()
        self.checkBox_5.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_2.raise_()

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
        self.save_btn.setCheckable(False)

        self.gridLayout_6.addWidget(self.save_btn, 1, 1, 1, 1)

        self.table_import_exceldata = QTableWidget(self.page3_import_data)
        if (self.table_import_exceldata.columnCount() < 10):
            self.table_import_exceldata.setColumnCount(10)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(6, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(7, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(8, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_import_exceldata.setHorizontalHeaderItem(9, __qtablewidgetitem31)
        self.table_import_exceldata.setObjectName(u"table_import_exceldata")
        self.table_import_exceldata.setLineWidth(0)
        self.table_import_exceldata.horizontalHeader().setDefaultSectionSize(120)

        self.gridLayout_6.addWidget(self.table_import_exceldata, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.page3_import_data)
        self.page4_users = QWidget()
        self.page4_users.setObjectName(u"page4_users")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(5)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.page4_users.sizePolicy().hasHeightForWidth())
        self.page4_users.setSizePolicy(sizePolicy7)
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
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(4, __qtablewidgetitem36)
        self.table_users.setObjectName(u"table_users")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.table_users.sizePolicy().hasHeightForWidth())
        self.table_users.setSizePolicy(sizePolicy8)
        self.table_users.setStyleSheet(u"")
        self.table_users.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_users.setAlternatingRowColors(True)
        self.table_users.verticalHeader().setVisible(False)

        self.gridLayout_5.addWidget(self.table_users, 0, 0, 1, 4)

        self.stackedWidget.addWidget(self.page4_users)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_10 = QGridLayout(self.page)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.table_bill_payedit = QTableWidget(self.page)
        if (self.table_bill_payedit.columnCount() < 12):
            self.table_bill_payedit.setColumnCount(12)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_bill_payedit.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.table_bill_payedit.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.table_bill_payedit.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.table_bill_payedit.setHorizontalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.table_bill_payedit.setHorizontalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.table_bill_payedit.setHorizontalHeaderItem(5, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.table_bill_payedit.setHorizontalHeaderItem(6, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.table_bill_payedit.setHorizontalHeaderItem(7, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.table_bill_payedit.setHorizontalHeaderItem(8, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.table_bill_payedit.setHorizontalHeaderItem(9, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.table_bill_payedit.setHorizontalHeaderItem(10, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.table_bill_payedit.setHorizontalHeaderItem(11, __qtablewidgetitem48)
        self.table_bill_payedit.setObjectName(u"table_bill_payedit")
        self.table_bill_payedit.setContextMenuPolicy(Qt.PreventContextMenu)
        self.table_bill_payedit.setAcceptDrops(True)
        self.table_bill_payedit.setLayoutDirection(Qt.RightToLeft)
        self.table_bill_payedit.setAutoFillBackground(True)
        self.table_bill_payedit.setStyleSheet(u"")
        self.table_bill_payedit.setFrameShadow(QFrame.Raised)
        self.table_bill_payedit.setLineWidth(0)
        self.table_bill_payedit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.table_bill_payedit.setAutoScrollMargin(16)
        self.table_bill_payedit.setDragEnabled(False)
        self.table_bill_payedit.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.table_bill_payedit.setDefaultDropAction(Qt.IgnoreAction)
        self.table_bill_payedit.setAlternatingRowColors(True)
        self.table_bill_payedit.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_bill_payedit.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table_bill_payedit.setTextElideMode(Qt.ElideRight)
        self.table_bill_payedit.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table_bill_payedit.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table_bill_payedit.setShowGrid(True)
        self.table_bill_payedit.setGridStyle(Qt.CustomDashLine)
        self.table_bill_payedit.setSortingEnabled(True)
        self.table_bill_payedit.setWordWrap(True)
        self.table_bill_payedit.setCornerButtonEnabled(True)
        self.table_bill_payedit.horizontalHeader().setCascadingSectionResizes(False)
        self.table_bill_payedit.horizontalHeader().setMinimumSectionSize(50)
        self.table_bill_payedit.horizontalHeader().setDefaultSectionSize(120)
        self.table_bill_payedit.horizontalHeader().setHighlightSections(True)
        self.table_bill_payedit.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_bill_payedit.horizontalHeader().setStretchLastSection(False)
        self.table_bill_payedit.verticalHeader().setVisible(True)
        self.table_bill_payedit.verticalHeader().setDefaultSectionSize(30)
        self.table_bill_payedit.verticalHeader().setProperty("showSortIndicator", False)

        self.gridLayout_10.addWidget(self.table_bill_payedit, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)

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

        self.bill_audits_btn = QPushButton(self.daohang)
        self.bill_audits_btn.setObjectName(u"bill_audits_btn")
        self.bill_audits_btn.setStyleSheet(u"background-color:  rgb(113, 113, 113);\n"
"color:rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/activity-feed-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.bill_audits_btn.setIcon(icon2)
        self.bill_audits_btn.setIconSize(QSize(24, 24))
        self.bill_audits_btn.setCheckable(True)
        self.bill_audits_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bill_audits_btn)

        self.bill_payedit_btn = QPushButton(self.daohang)
        self.bill_payedit_btn.setObjectName(u"bill_payedit_btn")
        self.bill_payedit_btn.setStyleSheet(u"background-color:  rgb(113, 113, 113);\n"
"color:rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/dollar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bill_payedit_btn.setIcon(icon3)
        self.bill_payedit_btn.setIconSize(QSize(24, 24))
        self.bill_payedit_btn.setCheckable(True)
        self.bill_payedit_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bill_payedit_btn)

        self.user_btn = QPushButton(self.daohang)
        self.user_btn.setObjectName(u"user_btn")
        self.user_btn.setStyleSheet(u"background-color:  rgb(113, 113, 113);\n"
"color:rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/group-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon4)
        self.user_btn.setIconSize(QSize(24, 24))
        self.user_btn.setCheckable(True)
        self.user_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.user_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.exit_btn = QPushButton(self.daohang)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon5)
        self.exit_btn.setIconSize(QSize(32, 32))
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
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/huoche.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon6)
        self.pushButton_8.setIconSize(QSize(32, 32))
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_8, 0, 0, 1, 1)

        self.line = QFrame(self.daohang)
        self.line.setObjectName(u"line")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(29)
        sizePolicy9.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy9)
        self.line.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.daohang, 0, 0, 2, 1)

        self.top = QFrame(self.centralwidget)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(559, 0))
        self.top.setStyleSheet(u"background-color: rgb(100,100, 100);")
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.top)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_4 = QPushButton(self.top)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background-color: rgb(130,130,130);\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.label = QLabel(self.top)
        self.label.setObjectName(u"label")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(1)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy10)
        self.label.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label)

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
        self.bill_audits_btn.toggled.connect(MainWindow.on_bill_audits_btn_toggled)
        self.bill_payedit_btn.toggled.connect(MainWindow.on_bill_payedit_btn_toggled)

        self.stackedWidget.setCurrentIndex(1)
        self.pushButton_8.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.table_bill_audits.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u5355\u53f7", None));
        ___qtablewidgetitem1 = self.table_bill_audits.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6838\u5b9e\u53f8\u673a", None));
        ___qtablewidgetitem2 = self.table_bill_audits.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u53f8\u673a", None));
        ___qtablewidgetitem3 = self.table_bill_audits.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u59cb\u53d1\u7f51\u70b9", None));
        ___qtablewidgetitem4 = self.table_bill_audits.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u7684\u7f51\u70b9", None));
        ___qtablewidgetitem5 = self.table_bill_audits.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u91d1\u989d", None));
        ___qtablewidgetitem6 = self.table_bill_audits.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u5ba1\u6838", None));
        ___qtablewidgetitem7 = self.table_bill_audits.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        ___qtablewidgetitem8 = self.table_bill_audits.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65f6\u95f4", None));
        ___qtablewidgetitem9 = self.table_bill_audits.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65f6\u95f4", None));
        ___qtablewidgetitem10 = self.table_bill_audits.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u5355\u53f7", None));
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u641c\u7d22", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u53f8\u673a\u59d3\u540d", None))
        self.cb_drivename_audits.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65e5\u671f", None))
        self.cb_startdate__audits.setText("")
        self.startdate__audits.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65e5\u671f", None))
        self.cb_enddate__audits.setText("")
        self.enddate__audits.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5ba1\u6838", None))
        self.cb_audits.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u65e5\u671f\u4ee5\n"
"\u4efb\u52a1\u5f00\u59cb\u65f6\u95f4\n"
"\u4e3a\u641c\u7d22\u6761\u4ef6", None))
        self.btn_serach_audits.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.btn_bill_update__audits.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0&\u4fdd\u5b58", None))
        ___qtablewidgetitem11 = self.table_bill_edit.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u8f93\u4efb\u52a1\u53f7", None));
        ___qtablewidgetitem12 = self.table_bill_edit.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u6838\u5b9e\u53f8\u673a", None));
        ___qtablewidgetitem13 = self.table_bill_edit.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u53f8\u673a\u59d3\u540d", None));
        ___qtablewidgetitem14 = self.table_bill_edit.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u724c\u53f7", None));
        ___qtablewidgetitem15 = self.table_bill_edit.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u59cb\u53d1\u7f51\u70b9", None));
        ___qtablewidgetitem16 = self.table_bill_edit.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u7684\u7f51\u70b9", None));
        ___qtablewidgetitem17 = self.table_bill_edit.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u91d1\u989d", None));
        ___qtablewidgetitem18 = self.table_bill_edit.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u5f00\u59cb\u65f6\u95f4", None));
        ___qtablewidgetitem19 = self.table_bill_edit.horizontalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u7ed3\u675f\u65f6\u95f4", None));
        ___qtablewidgetitem20 = self.table_bill_edit.horizontalHeaderItem(9)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u5355\u53f7", None));
        ___qtablewidgetitem21 = self.table_bill_edit.horizontalHeaderItem(10)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u641c\u7d22", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u53f8\u673a\u59d3\u540d", None))
        self.cb_drivename.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65e5\u671f(\u5927\u4e8e\u7b49\u4e8e)", None))
        self.cb_startdate.setText("")
        self.startdate.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65e5\u671f(\u5c0f\u4e8e\u7b49\u4e8e)", None))
        self.cb_enddate.setText("")
        self.enddate.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u5355\u53f7\uff08\u672a\u4f7f\u7528\uff09", None))
        self.checkBox_5.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u65e5\u671f\u4ee5\n"
"\u4efb\u52a1\u5f00\u59cb\u65f6\u95f4\n"
"\u4e3a\u641c\u7d22\u6761\u4ef6", None))
        self.btn_serach.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.btn_bill_update.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0&\u4fdd\u5b58", None))
        self.import_exceldata_btn.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165EXCEL\u6570\u636e", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e", None))
        ___qtablewidgetitem22 = self.table_import_exceldata.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u8fd0\u8f93\u53f7", None));
        ___qtablewidgetitem23 = self.table_import_exceldata.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u5f00\u59cb\u65f6\u95f4", None));
        ___qtablewidgetitem24 = self.table_import_exceldata.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u7ed3\u675f\u65f6\u95f4", None));
        ___qtablewidgetitem25 = self.table_import_exceldata.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u5355\u53f7", None));
        ___qtablewidgetitem26 = self.table_import_exceldata.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u59cb\u53d1\u7f51\u70b9", None));
        ___qtablewidgetitem27 = self.table_import_exceldata.horizontalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u7684\u7f51\u70b9", None));
        ___qtablewidgetitem28 = self.table_import_exceldata.horizontalHeaderItem(6)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u724c\u53f7", None));
        ___qtablewidgetitem29 = self.table_import_exceldata.horizontalHeaderItem(7)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u8d39\u8f66\u578b", None));
        ___qtablewidgetitem30 = self.table_import_exceldata.horizontalHeaderItem(8)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u53f8\u673a\u59d3\u540d", None));
        ___qtablewidgetitem31 = self.table_import_exceldata.horizontalHeaderItem(9)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u6838\u5b9e\u53f8\u673a", None));
        self.reload_btn.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.user_edit_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.add_user_btn.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e", None))
        self.del_user_btn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        ___qtablewidgetitem32 = self.table_users.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem33 = self.table_users.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None));
        ___qtablewidgetitem34 = self.table_users.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None));
        ___qtablewidgetitem35 = self.table_users.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u6743\u9650", None));
        ___qtablewidgetitem36 = self.table_users.horizontalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        ___qtablewidgetitem37 = self.table_bill_payedit.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u5355\u53f7", None));
        ___qtablewidgetitem38 = self.table_bill_payedit.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u4ed8\u6b3e", None));
        ___qtablewidgetitem39 = self.table_bill_payedit.horizontalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\u6838\u5b9e\u53f8\u673a", None));
        ___qtablewidgetitem40 = self.table_bill_payedit.horizontalHeaderItem(3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u53f8\u673a", None));
        ___qtablewidgetitem41 = self.table_bill_payedit.horizontalHeaderItem(4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\u59cb\u53d1\u7f51\u70b9", None));
        ___qtablewidgetitem42 = self.table_bill_payedit.horizontalHeaderItem(5)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u7684\u7f51\u70b9", None));
        ___qtablewidgetitem43 = self.table_bill_payedit.horizontalHeaderItem(6)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u91d1\u989d", None));
        ___qtablewidgetitem44 = self.table_bill_payedit.horizontalHeaderItem(7)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u5ba1\u6838", None));
        ___qtablewidgetitem45 = self.table_bill_payedit.horizontalHeaderItem(8)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        ___qtablewidgetitem46 = self.table_bill_payedit.horizontalHeaderItem(9)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65f6\u95f4", None));
        ___qtablewidgetitem47 = self.table_bill_payedit.horizontalHeaderItem(10)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65f6\u95f4", None));
        ___qtablewidgetitem48 = self.table_bill_payedit.horizontalHeaderItem(11)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u5355\u53f7", None));
        self.import_data_btn.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6570\u636e", None))
        self.bill_edit_btn.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u5355\u7f16\u8f91", None))
        self.bill_audits_btn.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u5355\u5ba1\u6838", None))
        self.bill_payedit_btn.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u5355\u4ed8\u6b3e", None))
        self.user_btn.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u7ba1\u7406", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u822a\u680f", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u9500", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237", None))
    # retranslateUi

