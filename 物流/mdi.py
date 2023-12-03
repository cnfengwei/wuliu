
import tkinter as tk
from tkinter import ttk,messagebox,filedialog,CENTER
import sqlite3,os
import pandas as pd


def extract_db_connection_info(file_path):
    # 获取当前文件所在的目录
    current_directory = os.path.dirname(__file__)
    # 构建绝对路径
    absolute_file_path = os.path.join(current_directory, file_path)
    return absolute_file_path
   
   
    # with open(absolute_file_path, 'r') as file:
    #     data = json.load(file)
    #     host = data['host']
    #     user = data['username']
    #     password = data['password']
    #     database = data['database']
    #     port =data['port']
    # return host, user, password, database,port

def open_file_dialog():
    root = Toplevel()#在当前的 Tk 实例上创建一个顶级窗口而不是新的 Tk 实例
    root.withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename(title="选择文件", filetypes=[("Excel files", "*.xlsx;*.xls")])
    return file_path

def get_column_names(table_name):
    cursor = mydb.cursor()
    cursor.execute(f"DESCRIBE {table_name}")
    columns = [column[0] for column in cursor.fetchall()]
    cursor.close()
    return columns

    # 设置 Treeview 的列
def set_treeview_columns(tree, columns):
    tree["columns"] = columns
    for col in columns:
        tree.heading(col, text=col, anchor=CENTER)
        
        tree.column(col, width=100)  # 调整列宽度，根据需要调整  

    # 插入数据到 Treeview
def insert_data_to_treeview(tree, data):
    tree.column("#0", width=10)  # 默认情况下，标识符列的名称是 "#0"
    for row in data:
        tree.insert("", "end", values=row)






def import_data():

    data_frame = ttk.Frame(root,borderwidth=5,relief='raised')
    data_frame.grid(column=1,row=0)
    data_tree= ttk.Treeview(data_frame)
    data_tree.grid(sticky='W E')
    # 设置Excel文件路径
    excel_file_path = open_file_dialog()
    # 读取Excel文件到DataFrame
    df = pd.read_excel(excel_file_path)
    i=0
    # 遍历 DataFrame 中的每一行
    for index, row in df.iterrows():
        # 将行数据转换为字典
        data = dict(row)
        
        # 检查数据库中是否已存在相同的记录，这里假设运输任务号是唯一标识
        with mydb.cursor() as cursor:
            sql_check_duplicate = "SELECT * FROM jd_bill WHERE 运输任务号 = %s"
            cursor.execute(sql_check_duplicate, (data['运输任务号'],))
            result = cursor.fetchone()

        # 如果数据库中没有相同的记录，插入数据
        if not result:
            # 插入数据的 SQL 语句
            sql_insert = "INSERT INTO jd_bill ({}) VALUES ({})".format(
                ', '.join(data.keys()),
                ', '.join('%({})s'.format(key) for key in data.keys())
            )
            
            # 使用连接执行 SQL 语句
            with mydb.cursor() as cursor:
                cursor.execute(sql_insert, data)
            i=i+1
    
    # 提交更改
    mydb.commit()
    print('导入'+str(i)+'条记录！')
   

class MainWindow:
    def __init__(self, root, mydb):
        self.root = root
        self.root.title('物流')
        self.root.geometry('800x600') 
        style = ttk.Style()
        functional_frame = ttk.Frame(root,borderwidth=5,relief='raised')
        functional_frame.grid(column=0,row=0,sticky='N')
        user_btn = ttk.Button(functional_frame, text="用户设置",width=20,command=user_set_window)
        style.configure('TButton', padding=(0, 10, 0, 10))
        user_btn.grid(column=0,row=0,sticky='W E')
        import_btn = ttk.Button(functional_frame, text="导入数据",width=20,command=import_data)
        style.configure('TButton', padding=(0, 10, 0, 10))
        import_btn.grid(column=0,row=1,sticky='W E')
        

        


class loginwindow:#登录窗口
    def __init__(self,root):

        self.root = root
        self.root.title("登录窗口")
       
        # 定义框架
        login_frame = ttk.Frame(root, padding=('30 30 40 50'))
        login_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.username_var = StringVar()
        self.password_var = StringVar()

        # 用户输入框
        login_usr_entry = ttk.Entry(login_frame, width=20, textvariable=self.username_var, font='宋体 18')
        login_usr_entry.grid(column=3, row=1, sticky='n')
        login_usr_entry.focus()
        # 当按下回车键时，焦点切换到密码输入框
        login_usr_entry.bind('<Return>', lambda event: login_psw_entry.focus())  

        # 密码输入框
        login_psw_entry = ttk.Entry(login_frame, width=20, textvariable=self.password_var, font='宋体 18')
        login_psw_entry.grid(column=3, row=2, sticky='n')
        login_psw_entry.bind('<Return>', lambda event: self.on_login())  # 当按下回车键时，执行登录操作
        # 标签
        ttk.Label(login_frame, text="用户名称", width=10).grid(column=2, row=1, sticky='w', pady=10)
        ttk.Label(login_frame, text="输入密码").grid(column=2, row=2, sticky='w', pady=10)

        ttk.Button(login_frame, text='登录', padding='5 5 10 5', command=self.on_login).grid(column=3, row=3, sticky='w', pady=15)
        ttk.Button(login_frame, text='取消', padding='5 5 10 5', command=root.destroy).grid(column=3, row=3, sticky='e')

    def on_login(self):
        
        
        
        cursor = mydb.cursor()
        
        # 从数据库中检索数据
        query = "SELECT * FROM users WHERE user = %s AND pwd = %s"
        cursor.execute(query, (self.username_var.get(), self.password_var.get()))
        print(self.username_var.get())
        # 检查用户是否存在
        if cursor.fetchone():
            
            cursor.close()

            # 登录成功：关闭登录窗口
            root.destroy()
            MainWindow(Tk(),mydb)
        else:
            messagebox.showerror("登录错误", "用户名或密码错误")



if __name__ == "__main__":
    root = tk.Tk()
    file_path = 'connection_info.json'
    host, user, password, database,port = extract_db_connection_info(file_path)

    try:#创建数据库的连接
        mydb = sqllite3.connect('wuliu.db')
    except Exception as e:
        messagebox.showerror("错误1", f"数据库连接失败: {str(e)}")
        SystemExit()
    MainWindow(root,mydb)
    #loginwindow(root)
    root.mainloop()
