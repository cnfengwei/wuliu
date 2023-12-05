import sqlite3
import sys
from PyQt6.QtWidgets import QMessageBox,QTableWidgetItem


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
            QMessageBox.warning(self, "数据库链接失败", str(e))
            sys.exit()

        self.my_cursor = self.my_connector.cursor()
        
    def get_connector(self):
        return self.my_connector

    def get_cursor(self):
        return self.my_cursor



    def conn_close(self):
        self.my_cursor.close()
        self.my_connector.close()

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
    
 
        

    def export_exceldata_to_db(self,tabeldata):
        self.tabeldata = tabeldata

        self.conn_close()
    def import_userdata(self,tableWidget,users):
        # 连接数据库
        self.conn_db()
        # 查询数据库中的users表数据
        self.my_cursor.execute("SELECT * FROM {}".format(users))
        data = self.my_cursor.fetchall()
        print(data)
        # 关闭数据库连接
        self.conn_close()

        # 将数据填入tableWidget中
        tableWidget.setRowCount(len(data))
        tableWidget.setColumnCount(len(data[0]))
        for i in range(len(data)):
            for j in range(len(data[0])):
                item = QTableWidgetItem(str(data[i][j]))
                tableWidget.setItem(i, j, item)
        