import sqlite3
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton,QFileDialog,QTableWidgetItem
from PyQt6.QtCore import pyqtSlot, QFile, QTextStream
from ui.sidebar_ui import Ui_MainWindow
import pandas as pd
from sql_calss import connect_db

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
        self.ui.import_data_btn.clicked.connect(self.on_import_data_btn_toggled)
        self.ui.savebtn.clicked.connect(self.on_savebtn_togggled)
        
       
       

    ## Function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)
    
    ## Function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)
        
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
            
    ## functions for changing menu page
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    # def on_dashborad_btn_1_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(1)

    # # def on_dashborad_btn_2_toggled(self):
    # #     self.ui.stackedWidget.setCurrentIndex(1)

    def on_import_data_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def open_file_dialog(self):
        # 显示文件选择对话框
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Excel Files (*.xlsx *.xls)")
        # file_dialog.setOptions(options)

        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            # 获取所选文件的路径
            selected_files = file_dialog.selectedFiles()
            excel_path = selected_files[0]
            return excel_path
        else:
            excel_path = ""
            
    def on_import_data_btn_toggled(self):
        excel_file_path = self.open_file_dialog()
        # 读取Excel文件到DataFrame
        df = pd.read_excel(excel_file_path)
        self.ui.tableWidget_2.setRowCount(df.shape[0])
        self.ui.tableWidget_2.setColumnCount(df.shape[1])
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[i, j]))
                self.ui.tableWidget_2.setItem(i, j, item)
        


    def on_savebtn_togggled(self):
        # 创建连接对象
        db_connector = connect_db()
        # 连接数据库
        db_connector.conn_db()

        # 获取连接对象和游标
        connector = db_connector.get_connector()
        cursor = db_connector.get_cursor()

        # 从数据库中检索数据
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='jdbill'")
        table_exists = cursor.fetchone() is not None
        if not table_exists:
            print("Error: Table 'jdbill' does not exist.")
            self.conn_close()
            return
        # 获取当前表中的所有运输任务号
        cursor.execute("SELECT 运输任务号 FROM jdbill")
        existing_task_numbers = set(row[0] for row in cursor.fetchall())
        # 插入数据
        for row in range(self.ui.tableWidget_2.rowCount()):
            task_number = self.ui.tableWidget_2.item(row, 0).text()  # 假设任务单号是第一列
            if task_number not in existing_task_numbers:
                # 只插入不存在的任务单号
                values = [self.ui.tableWidget_2.item(row, col).text() for col in range(self.ui.tableWidget_2.columnCount())]
                # cursor.execute(f"INSERT INTO jdbill VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)
                # 获取数据的数量
                data_count = len(values[0])

                # 打印数据的数量
                print(f"数据有 {data_count} 条记录")
                

        cursor.close()
        db_connector.conn_close()

        
    # def on_orders_btn_1_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(2)

    # def on_orders_btn_2_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(2)

    # def on_products_btn_1_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(3)

    # def on_products_btn_2_toggled(self, ):
    #     self.ui.stackedWidget.setCurrentIndex(3)

    # def on_customers_btn_1_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(4)

    # def on_customers_btn_2_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(4)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     ## loading style file
#     # with open("style.qss", "r") as style_file:
#     #     style_str = style_file.read()
#     # app.setStyleSheet(style_str)

#     ## loading style file, Example 2
#     style_file = QFile("style.qss")
#     style_file.open(QFile.ReadOnly | QFile.Text)
#     style_stream = QTextStream(style_file)
#     app.setStyleSheet(style_stream.readAll())


#     window = MainWindow()
#     window.show()

#     sys.exit(app.exec())



