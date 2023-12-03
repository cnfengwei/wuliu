from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import pandas as pd
from tkinter import filedialog
import json, os
from sqlalchemy import create_engine

from sqlalchemy import text
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

def import_data():
    try:
        # 读取 Excel 文件
        df = pd.read_excel("test.xlsx")
        # 插入数据到数据库
        df.to_sql("jdbill", mydb, index=False, if_exists="append")
        # 关闭数据库连接
        mydb.close()
        messagebox.showinfo("提示", "数据库连接成功")
    except Exception as e:
        messagebox.showerror("错误", f"数据库连接失败: {str(e)}")

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

# 读取Excel文件到DataFrame
df = pd.read_excel(excel_file_path)

# 创建数据库引擎
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")


df.to_sql(name='jd_bill', con=engine, if_exists='append', index=False)

# 关闭数据库连接
engine.dispose()

print("数据导入成功！")
if __name__ == "__main__":
    root = Tk()
    
    root.mainloop()