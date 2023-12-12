import sqlite3
import sys
from PySide6.QtWidgets import QMessageBox,QTableWidgetItem,QTableWidget,QCheckBox,QWidget,QHBoxLayout
from PySide6.QtCore import Qt
from tkinter import messagebox

#数据库连接的模块，用于数据库的连接和数据查询，更新和删除等sql语句执行
class connect_db():
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "test_user"
        self.password = "123456789"
        self.port = 3306
        self.database = "password_db"
        self.my_connector = None
        self.my_cursor = None
    
    def conn_db (self):
        try:
            self.my_connector = sqlite3.connect('wuliu.db')
            
        except Exception as e:
            messagebox.showerror("数据库链接失败", str(e))
            print(str(e))
            sys.exit()

        self.my_cursor = self.my_connector.cursor()
        
    def get_connector(self):
        return self.my_connector

    def get_cursor(self):
        return self.my_cursor
    #数据库关闭
    def conn_close(self):
        self.my_cursor.close()
        self.my_connector.close()
    #登录检查
    def check_login(self,user_name,password):
        self.username = user_name
        self.password = password
        self.conn_db()
        
        # 从数据库中检索数据
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        self.my_cursor.execute(query, (self.username, self.password))
        
        # 检查用户是否存在
        result = self.my_cursor.fetchall()
        self.conn_close()
        return result

    #用户列表输入数据
    def import_userdata(self,tableWidget: QTableWidget,users):
        self.conn_db()
        # 查询用户表
        self.my_cursor.execute("SELECT * FROM {}".format(users))
        data = self.my_cursor.fetchall()
        # 关闭数据库连接
        self.conn_close()

        # 设置 table rowCount 和 columnCount
        tableWidget.setRowCount(len(data))
        tableWidget.setColumnCount(len(data[0]))

        # 将数据填充到 table widget
        for i in range(len(data)):
            for j in range(len(data[0])):
                item = QTableWidgetItem(str(data[i][j]))
                tableWidget.setItem(i, j, item)

        
    #新增用户信息，记录插入到数据库
    def adduser(self,username,password,qx,memo):
        self.username = username
        self.password = password
        self.qx = qx
        self.memo = memo
        self.conn_db()
        query = "select * from users where username = ?"
        self.my_cursor.execute(query,[self.username])
        result = self.my_cursor.fetchall()
        #查询该用户是否存在，如果不存在，插入记录
        if len(result) > 0 :
            messagebox.showerror("提示", "已有该用户名存在，请重新输入")
            return 
        else:
            query = "INSERT INTO users (username, password, qx, memo) VALUES (?, ?, ?, ?); "
            self.my_cursor.execute(query, (self.username, self.password,self.qx,self.memo))
            self.my_connector.commit()
            self.conn_close()
            return 1
    #将修改后的用户信息提交数据库 
    def updateuser(self,username,password,qx,memo,id):
        
        self.id = int(id)
        self.conn_db()
        query = "update users SET username = ?,password=?,qx=?,memo=? where id=?"
        self.my_cursor.execute(query,[username,password,qx,memo,id])
        
        
        if self.my_cursor.rowcount > 0:
            self.my_connector.commit()
            return 1
        else:
            messagebox.showerror("提示", self.my_connector.Error())
        self.conn_close()

    #将需要修改的用户信息返回给usewindow
    def edituser(self,userid):
        self.userid =int(userid)
        self.conn_db()
        query = "select * from users where id = ?"
        self.my_cursor.execute(query,[self.userid])
        result = self.my_cursor.fetchall()
        return result

    #删除选择的用户       
    def deleteuser(self,id):
        
        self.conn_db()
        self.id= int(id)
        query = "DELETE FROM users WHERE id = ?"
        self.my_cursor.execute(query, [self.id])
        self.my_connector.commit()
        self.conn_close
        messagebox.showinfo("成功","删除记录成功")

    def importbilldata(self,tableWidget):
        self.conn_db()
        # 查询用户表
        self.my_cursor.execute("SELECT \"运输任务号\", \"核实司机\", \"三方司机姓名\" ,\"车牌号\",\
        \"始发网点\",\"目的网点\", \"金额\", \"任务开始时间\", \"任务结束时间\",\"三方单号\", \"备注\" FROM bill_view")
        data = self.my_cursor.fetchall()
        # 关闭数据库连接
        self.conn_close()
        
        # 设置 table rowCount 和 columnCount

        tableWidget.setRowCount(len(data))
        tableWidget.setColumnCount(len(data[0]))

        # 将数据填充到 table widget
        for i in range(len(data)):
            for j in range(len(data[0])):
                item = QTableWidgetItem(str(data[i][j]))
                tableWidget.setItem(i, j, item)

    def serach_bill_audits(self,tableWidget,query,drivename,startdate,enddate):
        self.conn_db()
        
        
        self.my_cursor.execute(query,{'drivename':drivename,'startdate':startdate,'enddate':enddate})
        data = self.my_cursor.fetchall()
        # 关闭数据库连接
        self.conn_close()
        # 设置 table rowCount 和 columnCount

        tableWidget.setRowCount(len(data))
        tableWidget.setColumnCount(len(data[0]))
        # 设置第六列为checkbox
        
             
        # 将数据填充到 table widget
        for i in range(len(data)):
            for j in range(len(data[0])):
                if j != 6:
                    item = QTableWidgetItem(str(data[i][j]))
                    item.setTextAlignment(Qt.AlignCenter)
                    tableWidget.setItem(i, j, item)
                else: 
                    checkbox = QCheckBox()
                    checkbox.setChecked(data[i][6])
                    # 将复选框添加到表格中
                    
                    # tableWidget.setCellWidget(i, 6, checkbox)
                    # tableWidget.setColumnWidth(6, 50)
                    container_widget = QWidget()
                    layout = QHBoxLayout(container_widget)
                    layout.addWidget(checkbox)
                    layout.setAlignment(Qt.AlignCenter)
                    layout.setContentsMargins(0, 0, 0, 0)
                    
                    # 将容器窗口设置为单元格小部件
                    tableWidget.setCellWidget(i, 6, container_widget)
                    
                    tableWidget.setColumnWidth(6, 50)
                    
                    



                    
                    
    def serachbilldata(self,tableWidget,query,drivename,startdate,enddate):
        self.conn_db()
        
        
        self.my_cursor.execute(query,{'drivename':drivename,'startdate':startdate,'enddate':enddate})
        data = self.my_cursor.fetchall()
        # 关闭数据库连接
        self.conn_close()
        if data == []:
            messagebox.showerror("查询结果", "没有符合条件的记录")
            return
        #tablewidget.setRowCount(0)
        # 设置 table rowCount 和 columnCount
        tableWidget.setRowCount(len(data))
        tableWidget.setColumnCount(len(data[0]))

        # 将数据填充到 table widget
        for i in range(len(data)):
            for j in range(len(data[0])):
                item = QTableWidgetItem(str(data[i][j]))
                tableWidget.setItem(i, j, item)
    
    def update_billmount(self,data):
        self.conn_db()
        for data_row in data:
            query ="update bill_mount set 金额 = ? where 任务单号 = ?"
            self.my_cursor.execute(query,(data_row[1],data_row[0]))
        self.my_connector.commit()
        messagebox.showerror("更新", "记录更新成功")
        self.conn_close()