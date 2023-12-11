
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton,QFileDialog,QTableWidgetItem,QMessageBox
from PySide6.QtCore import Slot
from ui.mainwindow_ui import Ui_MainWindow
import pandas as pd
from sql_class import connect_db
from userwindow import adduser

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mydb = connect_db()
        self.adduser = adduser()

        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.import_exceldata_btn.clicked.connect(self.import_exceldata_btn_toggled)
        self.ui.add_user_btn.clicked.connect(self.add_user_btn_clicked)
        self.ui.reload_btn.clicked.connect(self.on_user_btn_clicked)
        self.ui.del_user_btn.clicked.connect(self.user_del_btn_clicked)
        self.ui.user_edit_btn.clicked.connect(self.user_edit_btn_clicked)
    ## 改变页面到用户页面, 并加载数据库中表users的数据 
    def on_user_btn_clicked(self):
        
        self.ui.stackedWidget.setCurrentIndex(4)
        self.mydb.import_userdata(self.ui.table_users,'users')
        
    # def on_stackedWidget_currentChanged(self):
      
    #     cur_index=self.ui.stackedWidget.currentIndex()
    
    #导入数据按钮激活，并且切换到导入数据的索引页
    def on_import_data_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        
    # 显示文件选择对话框，并获得excel路径
    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Excel Files (*.xlsx *.xls)")
        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            # 获取所选文件的路径
            selected_files = file_dialog.selectedFiles()
            excel_path = selected_files[0]
            return excel_path
        else:
            return None

    #将excel中数据导入到tableWidget       
    def import_exceldata_btn_toggled(self):
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
        df = pd.read_excel(excel_file_path)
        self.ui.table_import_exceldata.setRowCount(df.shape[0])
        self.ui.table_import_exceldata.setColumnCount(df.shape[1])
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[i, j]))
                self.ui.table_import_exceldata.setItem(i, j, item)
    
    #导入在tablewidget中的数据到数据库
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
            for row in range(self.ui.table_import_exceldata.rowCount()):
                task_number = self.ui.table_import_exceldata.item(row, 0).text()  # 假设任务单号是第一列
                if task_number not in existing_task_numbers:
                    # 只插入不存在的任务单号
                    values = [self.ui.table_import_exceldata.item(row, col).text() for col in range(self.ui.table_import_exceldata.columnCount())]
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
   
    def on_bill_edit_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    
    #用户新增按钮激活   
    def add_user_btn_clicked(self):
        
        self.adduser.show()
    
    #用户删除
    def user_del_btn_clicked(self):
        row = self.ui.table_users.currentRow()
        id = self.ui.table_users.item(row, 0).text()
        
        if row >= 0:
            self.ui.table_users.removeRow(row)
            self.mydb.deleteuser(id)
            
           

    
    def user_edit_btn_clicked(self):
        row = self.ui.table_users.currentRow()
        id = self.ui.table_users.item(row, 0).text()
        
    
    def on_bill_serach_btn_toggled(self):
        
        self.ui.stackedWidget.setCurrentIndex(1)








