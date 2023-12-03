from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import pandas as pd
from tkinter import filedialog
import json, os
from sqlalchemy import create_engine,text

def extract_db_connection_info(file_path):
    # 获取当前文件所在的目录
    current_directory = os.path.dirname(__file__)
    
    # 构建绝对路径
    absolute_file_path = os.path.join(current_directory, file_path)
    with open(absolute_file_path, 'r') as file:
        data = json.load(file)
        host = data['host']
        user = data['username']
        password = data['password']
        database = data['database']
        port =data['port']
    return host, user, password, database,port



def open_file_dialog():
    root=Tk()
    root.withdraw()  # 隐藏主窗口

    file_path = filedialog.askopenfilename(title="选择文件", filetypes=[("Excel files", "*.xlsx;*.xls")])
   

    return file_path

def extract_excelpath(excel_file_path):
    current_directory = os.path.dirname(__file__)
    absolute_file_path = os.path.join(current_directory, excel_file_path)

    return absolute_file_path


file_path = 'connection_info.json'
host, user, password, database,port = extract_db_connection_info(file_path)

try:
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database,
        port=port
    )

except Exception as e:
    messagebox.showerror("错误1", f"数据库连接失败: {str(e)}")
    SystemExit()

# 设置Excel文件路径

excel_file_path = open_file_dialog()

# 读取Excel文件到DataFrame，指定index_col=None
df = pd.read_excel(excel_file_path)


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

# 提交更改
mydb.commit()

# 关闭连接
mydb.close()
    




SystemExit()
