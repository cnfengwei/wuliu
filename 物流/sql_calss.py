import sqlite3
import sys
from PyQt6.QtWidgets import QMessageBox

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
    
    def import_exceldata_save(self):
        self.tabeldata = tableWidget_2
        self.conn_db()
        
        # 从数据库中检索数据
        self.my_cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='jdbill'")
        table_exists = self.my_cursor.fetchone() is not None

        if not table_exists:
            print("Error: Table 'jdbill' does not exist.")
            self.conn_close()
            return

        # 获取当前表中的所有任务单号
        self.my_cursor.execute("SELECT 运输任务号 FROM jdbill")
        
        existing_task_numbers = set(row[0] for row in self.my_cursor.fetchall())
        print(str(existing_task_numbers))
        # 插入数据
        # for row in range(self.table_widget.rowCount()):
        #     task_number = self.table_widget.item(row, 0).text()  # 假设任务单号是第一列
        #     if task_number not in existing_task_numbers:
        #         # 只插入不存在的任务单号
        #         values = [self.tabledata.item(row, col).text() for col in range(self.table_widget.columnCount())]
        #         self.my_cursor.execute(f"INSERT INTO jdbill VALUES (?, ?, ?, ?)", values)

        # 提交并关闭连接
        self.my_connector.commit()
        self.conn_close()

    def export_exceldata_to_db(self,tabeldata):
        self.tabeldata = tabeldata

        self.conn_close()
