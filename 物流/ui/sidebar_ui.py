# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc
import resource_rc
import resource_rc
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(987, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.full_menu_widget = QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName(u"full_menu_widget")
        self.verticalLayout_4 = QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo_label_2 = QLabel(self.full_menu_widget)
        self.logo_label_2.setObjectName(u"logo_label_2")
        self.logo_label_2.setMinimumSize(QSize(40, 40))
        self.logo_label_2.setMaximumSize(QSize(40, 40))
        self.logo_label_2.setPixmap(QPixmap(u"../icon/Logo.png"))
        self.logo_label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo_label_2)

        self.logo_label_3 = QLabel(self.full_menu_widget)
        self.logo_label_3.setObjectName(u"logo_label_3")
        font = QFont()
        font.setPointSize(15)
        self.logo_label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.logo_label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.home_btn_2 = QPushButton(self.full_menu_widget)
        self.home_btn_2.setObjectName(u"home_btn_2")
        icon = QIcon()
        icon.addFile(u"../icon/home-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn_2.setIcon(icon)
        self.home_btn_2.setIconSize(QSize(14, 14))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_btn_2)

        self.import_data_btn_2 = QPushButton(self.full_menu_widget)
        self.import_data_btn_2.setObjectName(u"import_data_btn_2")
        icon1 = QIcon()
        icon1.addFile(u"../icon/dashboard-5-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.import_data_btn_2.setIcon(icon1)
        self.import_data_btn_2.setIconSize(QSize(14, 14))
        self.import_data_btn_2.setCheckable(True)
        self.import_data_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.import_data_btn_2)

        self.orders_btn_2 = QPushButton(self.full_menu_widget)
        self.orders_btn_2.setObjectName(u"orders_btn_2")
        icon2 = QIcon()
        icon2.addFile(u"../icon/activity-feed-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.orders_btn_2.setIcon(icon2)
        self.orders_btn_2.setIconSize(QSize(14, 14))
        self.orders_btn_2.setCheckable(True)
        self.orders_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.orders_btn_2)

        self.products_btn_2 = QPushButton(self.full_menu_widget)
        self.products_btn_2.setObjectName(u"products_btn_2")
        icon3 = QIcon()
        icon3.addFile(u"../icon/product-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.products_btn_2.setIcon(icon3)
        self.products_btn_2.setIconSize(QSize(14, 14))
        self.products_btn_2.setCheckable(True)
        self.products_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.products_btn_2)

        self.customers_btn_2 = QPushButton(self.full_menu_widget)
        self.customers_btn_2.setObjectName(u"customers_btn_2")
        icon4 = QIcon()
        icon4.addFile(u"../icon/group-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.customers_btn_2.setIcon(icon4)
        self.customers_btn_2.setIconSize(QSize(14, 14))
        self.customers_btn_2.setCheckable(True)
        self.customers_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.customers_btn_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 373, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exit_btn_2 = QPushButton(self.full_menu_widget)
        self.exit_btn_2.setObjectName(u"exit_btn_2")
        icon5 = QIcon()
        icon5.addFile(u"../icon/account-logout-64.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn_2.setIcon(icon5)
        self.exit_btn_2.setIconSize(QSize(14, 14))

        self.verticalLayout_4.addWidget(self.exit_btn_2)


        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.horizontalSpacer = QSpacerItem(236, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_input = QLineEdit(self.widget)
        self.search_input.setObjectName(u"search_input")

        self.horizontalLayout.addWidget(self.search_input)

        self.search_btn = QPushButton(self.widget)
        self.search_btn.setObjectName(u"search_btn")
        icon6 = QIcon()
        icon6.addFile(u"../icon/search-13-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon6)

        self.horizontalLayout.addWidget(self.search_btn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(236, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.user_btn = QPushButton(self.widget)
        self.user_btn.setObjectName(u"user_btn")
        icon7 = QIcon()
        icon7.addFile(u"../icon/user-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.user_btn)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.import_data_btn = QPushButton(self.page_2)
        self.import_data_btn.setObjectName(u"import_data_btn")

        self.gridLayout_3.addWidget(self.import_data_btn, 1, 0, 1, 1)

        self.savebtn = QPushButton(self.page_2)
        self.savebtn.setObjectName(u"savebtn")

        self.gridLayout_3.addWidget(self.savebtn, 1, 1, 1, 1)

        self.tableWidget_2 = QTableWidget(self.page_2)
        if (self.tableWidget_2.columnCount() < 10):
            self.tableWidget_2.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_3.addWidget(self.tableWidget_2, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_5 = QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_6 = QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_7 = QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_9 = QLabel(self.page_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_8 = QGridLayout(self.page_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.user_add_btn = QPushButton(self.page_7)
        self.user_add_btn.setObjectName(u"user_add_btn")

        self.gridLayout_8.addWidget(self.user_add_btn, 1, 0, 1, 1)

        self.user_del_btn = QPushButton(self.page_7)
        self.user_del_btn.setObjectName(u"user_del_btn")

        self.gridLayout_8.addWidget(self.user_del_btn, 1, 1, 1, 1)

        self.user_save_btn = QPushButton(self.page_7)
        self.user_save_btn.setObjectName(u"user_save_btn")

        self.gridLayout_8.addWidget(self.user_save_btn, 1, 2, 1, 1)

        self.table_users = QTableWidget(self.page_7)
        if (self.table_users.columnCount() < 5):
            self.table_users.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setText(u"id");
        self.table_users.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.table_users.setObjectName(u"table_users")

        self.gridLayout_8.addWidget(self.table_users, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.page_7)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.exit_btn_2.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_label_2.setText("")
        self.logo_label_3.setText(QCoreApplication.translate("MainWindow", u"Sidebar", None))
        self.home_btn_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.import_data_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5bfc\u5165", None))
        self.orders_btn_2.setText(QCoreApplication.translate("MainWindow", u"Orders", None))
        self.products_btn_2.setText(QCoreApplication.translate("MainWindow", u"Products", None))
        self.customers_btn_2.setText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.exit_btn_2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.search_btn.setText("")
        self.user_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.import_data_btn.setText(QCoreApplication.translate("MainWindow", u"\u4ece\u6587\u4ef6\u5bfc\u5165\u6570\u636e", None))
        self.savebtn.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e\u5230\u6570\u636e\u5e93", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u5355\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65f6\u95f4", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65f6\u95f4", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u5355\u53f7", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u59cb\u53d1\u7f51\u70b9", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u7684\u7f51\u70b9", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u724c\u53f7", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u8d39\u8f66\u578b", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u65b9\u53f8\u673a", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u6838\u5b9e\u53f8\u673a", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Orders Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Product Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Customers Page", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Search Page", None))
        self.user_add_btn.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e", None))
        self.user_del_btn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.user_save_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        ___qtablewidgetitem10 = self.table_users.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None));
        ___qtablewidgetitem11 = self.table_users.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None));
        ___qtablewidgetitem12 = self.table_users.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u6743\u9650", None));
        ___qtablewidgetitem13 = self.table_users.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
    # retranslateUi

