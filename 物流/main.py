
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton,QFileDialog,QTableWidgetItem,QMessageBox
from PySide6.QtCore import Slot, QFile, QTextStream
from ui.sidebar_ui import Ui_MainWindow
import pandas as pd
from sql_class import connect_db


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mydb = connect_db()
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
   
    ## Function for searching
    @Slot()
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)
    
    ## 改变页面到用户页面, 并加载数据库中的数据
    @Slot()
    def on_user_btn_clicked(self):
        
        self.ui.stackedWidget.setCurrentIndex(6)
        self.mydb.import_userdata(self.ui.table_users,'users')
        
    ## Change QPushButton Checkable status when stackedWidget index changed
    @Slot()
    def on_stackedWidget_currentChanged(self):
        # btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
        #             + self.ui.full_menu_widget.findChildren(QPushButton)
        cur_index=self.ui.stackedWidget.currentIndex()
        print(cur_index)
        
        # for btn in btn_list:
        #     if index in [5, 6]:
        #         btn.setAutoExclusive(False)
        #         btn.setChecked(False)
        #     else:
        #         btn.setAutoExclusive(True)  
  
    #当home_btn_2被点击
    @Slot()
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        
    #数据导入按钮被点击
    @Slot()
    def on_import_data_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.tableWidget_2.setRowCount(0)
    # 显示文件选择对话框，并获得excel路径
    @Slot()
    def open_file_dialog(self):
        
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
            return None
    #将excel中数据导入到tableWidget
    @Slot()     
    def on_import_data_btn_toggled(self):
        excel_file_path = self.open_file_dialog()
        if excel_file_path is None:
            return
        try:
            df = pd.read_excel(excel_file_path)
        except ValueError as e:
            error_message = f"导入 Excel 文件出错：{str(e)}"
            QMessageBox.warning(self, "导入错误", error_message)
            # 获取错误信息的元组
            error_args = e.args

            # 打印错误信息
            print(error_args)
            return
        # 读取Excel文件到DataFrame
        #df = pd.read_excel(excel_file_path)
        self.ui.tableWidget_2.setRowCount(df.shape[0])
        self.ui.tableWidget_2.setColumnCount(df.shape[1])
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[i, j]))
                self.ui.tableWidget_2.setItem(i, j, item)
    
    #导入在tablewidget中的数据到数据库
    @Slot()
    def on_savebtn_toggled(self):
       
        # 连接数据库
        self.mydb.conn_db()

        # 获取连接对象和游标
        connector = self.mydb.get_connector()
        cursor = self.mydb.get_cursor()

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
        i=0
        try:
            # 插入数据
            for row in range(self.ui.tableWidget_2.rowCount()):
                task_number = self.ui.tableWidget_2.item(row, 0).text()  # 假设任务单号是第一列
                if task_number not in existing_task_numbers:
                    # 只插入不存在的任务单号
                    values = [self.ui.tableWidget_2.item(row, col).text() for col in range(self.ui.tableWidget_2.columnCount())]
                    cursor.execute("INSERT INTO jdbill VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)", values)
                    i += 1
                    
            connector.commit() 
               
        except Exception as e:
           QMessageBox.warning(self,'更新失败',str(e))
        msg=QMessageBox()
        msg.setText('更新数据'+str(i)+'记录')  
        msg.exec() 
        cursor.close()
        self.mydb.conn_close()

        

    @Slot()
    def on_orders_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    #点击新增按钮
    @Slot()
    def on_user_add_btn_toggled(self):
        rowCount = self.ui.table_users.rowCount()
        self.ui.table_users.insertRow(rowCount)
        for column in range(self.ui.table_users.columnCount()):
            self.ui.table_users.setItem(rowCount, column, QTableWidgetItem(None))
    #点击删除按钮
    @Slot()
    def on_user_del_btn_toggled(self):
        row = self.ui.table_users.currentRow()
        if row >= 0:
            self.ui.table_users.removeRow(row)
    @Slot()
    def on_user_save_btn_toggled(self):
        data = []
        for row in range(self.ui.table_users.rowCount()):
            data.append({
                "id": self.ui.table_users.item(row, 0).text(),
                "username": self.ui.table_users.item(row, 1).text(),
                "password": self.ui.table_users.item(row, 1).text(),
                "qx": self.ui.table_users.item(row, 1).text(),
                "memo": self.ui.table_users.item(row, 1).text(),
            })
        print(data)
        for user in data:
            if user["id"] == '':
                print('add')
            else:
                print('update')
    # def on_products_btn_1_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(3)

    # def on_products_btn_2_toggled(self, ):
    #     self.ui.stackedWidget.setCurrentIndex(3)

    # def on_customers_btn_1_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(4)

    # def on_customers_btn_2_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(4)






