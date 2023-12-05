from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog,QMessageBox
from sql_class import connect_db


# 登录窗口
class LoginWindow(QDialog):
    def __init__(self,main_window):
        super(LoginWindow,self).__init__()
        loadUi("./ui/loginwindow.ui", self)
        self.main_window=main_window
        self.mydb = connect_db()
        self.mydb.conn_db()
        
        self.btn_login.clicked.connect(self.login)
        self.label_message.setText('数据库已连接')
    
    def login(self):
        self.username = self.entry_user.text()
        self.password = self.entry_password.text()
    
        if not self.username and not self.password:
            self.warning_messagebox("请输入用户名和密码!")
            return

        result = self.mydb.check_login(self.username,self.password)
        if len(result) == 1 :
            
            self.main_window.show()
            
            self.close()
        else:
            print('no')
