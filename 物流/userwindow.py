from ui.usereditwindow_ui import Ui_user_edit_window
from PySide6.QtWidgets import QDialog,QMessageBox
from sql_class import connect_db

class adduser(QDialog):
    def __init__(self):
        super(adduser,self).__init__()
        self.ui = Ui_user_edit_window()
        self.ui.setupUi(self)
        self.windowTitle="新增"
        self.mydb = connect_db()
        

    def accept(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        qx = self.ui.qx.currentText()
        memo = self.ui.memo.toPlainText()

        if not username and not password:
            QMessageBox.information(self,"错误","请输入用户名和密码!")
            return

        if self.mydb.adduser(username,password,qx,memo) == 1 :
           
            self.close()
            QMessageBox.information(self,"成功","用户添加成功！")

class edituser(QDialog):
    def __init__(self,userid):
        super(edituser,self).__init__()
        self.ui = Ui_user_edit_window()
        self.ui.setupUi(self)
        self.windowTitle="修改"
        self.userid=userid
        self.mydb = connect_db()
        result = self.mydb.edituser(self.userid)
        self.ui.username.setText(result[0][1])
        self.ui.password.setText(result[0][2])
        self.ui.qx.setCurrentIndex(int(result[0][3]))
        self.ui.memo.insertPlainText(result[0][4])
        
    def accept(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        qx = self.ui.qx.currentText()
        memo = self.ui.memo.toPlainText()
        id = int(self.userid)
        if self.mydb.updateuser(username,password,qx,memo,id) == 1 :
           QMessageBox.information(self,"成功","用户更改成功！")
           self.close()
        