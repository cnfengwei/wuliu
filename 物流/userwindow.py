from ui.usereditwindow_ui import Ui_user_edit_window
from PySide6.QtWidgets import QDialog,QMessageBox
from sql_class import connect_db
class userwindow(QDialog):
    def __init__(self):
        super(userwindow,self).__init__()
        self.ui = Ui_user_edit_window()
        self.ui.setupUi(self)
        self.mydb = connect_db()
        

    def accept(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        qx = self.ui.qx.currentText()
        memo = self.ui.memo.toPlainText()

        if not username and not password:
            self.warning_messagebox("请输入用户名和密码!")
            return

        if self.mydb.adduser(username,password,qx,memo) == 1 :
           
            self.close()
            QMessageBox.information(self,"成功","用户添加成功！")
      