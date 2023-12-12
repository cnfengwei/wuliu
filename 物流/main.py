
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton,QFileDialog,QTableWidgetItem,QMessageBox,QCheckBox
from ui.mainwindow_ui import Ui_MainWindow
import pandas as pd
from sql_class import connect_db
from userwindow import adduser,edituser

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
        self.ui.btn_serach.clicked.connect(self.btn_serach_clicked)#运单编辑页面的搜索按钮
        self.ui.btn_bill_update.clicked.connect(self.update_bill_mount)#运单编辑页面的保存按钮
        self.ui.btn_serach_audits.clicked.connect(self.btn_serach_audits_clicked)#运单审核页面的搜索按钮
        self.ui.save_btn.clicked.connect(self.on_savebtn_toggled)#导入数据页面，保存按钮
        self.ui.btn_bill_update__audits.clicked.connect(self.update_bill_audits)#运单审核页面的保存按钮
        
    
        
    # def on_stackedWidget_currentChanged(self):
      
    #     cur_index=self.ui.stackedWidget.currentIndex()
    
    def on_bill_audits_btn_toggled(self): 
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_bill_edit_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        #self.mydb.importbilldata(self.ui.table_bill_edit)

    #导入数据按钮激活，并且切换到导入数据的索引页
    def on_import_data_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    ## 改变页面到用户页面, 并加载数据库中表users的数据 
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.mydb.import_userdata(self.ui.table_users,'users')
      
    def on_bill_payedit_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        
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
       
    #用户新增按钮激活   
    def add_user_btn_clicked(self):       
        self.adduser.show()
    
    #用户删除，从sqlclass执行操作
    def user_del_btn_clicked(self):
        row = self.ui.table_users.currentRow()
        id = self.ui.table_users.item(row, 0).text()       
        if row >= 0:
            self.ui.table_users.removeRow(row)
            self.mydb.deleteuser(id)
        QMessageBox.information(self,'提示','删除成功')
           

    #用户修改信息，将选择行的序号传递给userwindow，加载该用户的信息
    def user_edit_btn_clicked(self):
        row = self.ui.table_users.currentRow()
        id = self.ui.table_users.item(row, 0).text()
        self.edituser=edituser(userid=id)
        self.edituser.show()

    # 根据选项设定搜索条件，主要是增加了审核这个选项   
    def btn_serach_audits_clicked(self):
        query = "SELECT \"运输任务号\", \"核实司机\", \"三方司机姓名\" ,\
        \"始发网点\",\"目的网点\", \"金额\", \"审核\",\"备注\",\"任务开始时间\", \"任务结束时间\",\"三方单号\" FROM bill_view where \
        CASE WHEN :drivename <> '' THEN  核实司机= :drivename ELSE 1=1 END \
         AND CASE WHEN :startdate <> '' THEN 任务开始时间 >= :startdate ELSE 1=1 END \
          AND CASE WHEN :enddate <> '' THEN 任务开始时间 <= :enddate ELSE 1=1 END \
          AND CASE WHEN :audits <> '' THEN 审核 = :audits ELSE 1=1 END "
        # ******日期格式必须为yyyy-mm-dd，yyyy-m-d和yyyy/m/d数据库搜索不到记录******
        if self.ui.cb_drivename_audits.isChecked():
            drivename = self.ui.drivename__audits.text()
        else:
            drivename=""
        if self.ui.cb_startdate__audits.isChecked():
            startdate = self.ui.startdate__audits.text()
        else:
            startdate=""
        if self.ui.cb_enddate__audits.isChecked():
            enddate= self.ui.enddate__audits.text()
        else:
            enddate=""       
        if self.ui.cb_audits.isChecked() :
           audits = 1
        else:
            audits= 0      
        self.mydb.serach_bill_audits(self.ui.table_bill_audits,query,drivename,startdate,enddate,audits)
    
    #在运单编辑表中填充搜索结果
    def btn_serach_clicked(self):     
        query = "SELECT \"运输任务号\", \"核实司机\", \"三方司机姓名\" ,\"车牌号\",\
        \"始发网点\",\"目的网点\", \"金额\", \"任务开始时间\", \"任务结束时间\",\"三方单号\", \"备注\" FROM bill_view where \
        CASE WHEN :drivename <> '' THEN  核实司机= :drivename ELSE 1=1 END \
         AND CASE WHEN :startdate <> '' THEN 任务开始时间 >= :startdate ELSE 1=1 END \
          AND CASE WHEN :enddate <> '' THEN 任务开始时间 <= :enddate ELSE 1=1 END  "
        # ******日期格式必须为yyyy-mm-dd，yyyy-m-d和yyyy/m/d数据库搜索不到记录******
        if self.ui.cb_drivename.isChecked():
            drivename = self.ui.drivename.text()
        else:
            drivename=""
        if self.ui.cb_startdate.isChecked():
            startdate = self.ui.startdate.text()
        else:
            startdate=""
        if self.ui.cb_enddate.isChecked():
            enddate= self.ui.enddate.text()
        else:
            enddate=""       
        self.mydb.serachbilldata(self.ui.table_bill_edit,query,drivename,startdate,enddate)

    #运单审核页面将审核的数据保存到数据库
    def update_bill_audits(self):       
        if self.ui.table_bill_audits.rowCount() ==0 :
           return     
        data = []
        for i in range(self.ui.table_bill_audits.rowCount()):            
            data_col0 = self.ui.table_bill_audits.item(i, 0).text()# 获取第0列数据           
            cell_widget = self.ui.table_bill_audits.cellWidget(i, 6)# 获取第6列数据
            if cell_widget is not None:
                checkbox = cell_widget.findChild(QCheckBox)
                if checkbox is not None:
                    data_col6 = checkbox.isChecked()
            data.append((data_col0,data_col6))
        if self.mydb.update_billaudits(data) == 1:
                self.ui.table_bill_audits.setRowCount(0)


    #运单编辑页面将运单金额的数据保存到数据库
    def update_bill_mount(self):
        data = []
        for row in range(self.ui.table_bill_edit.rowCount()):
            data_col0 = self.ui.table_bill_edit.item(row, 0).text()
            data_col6 = self.ui.table_bill_edit.item(row, 6).text()
            data.append((data_col0,data_col6))
        self.mydb.update_billmount(data)






