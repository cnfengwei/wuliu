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
df = pd.read_excel(excel_file_path, index_col=None)

# 创建数据库引擎
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")

# 在插入数据之前检查数据库中是否已经存在相同主键值的记录
for index, row in df.iterrows():
    primary_key_value = row['运输任务号']
    
    # 创建连接
    connection = engine.connect()
    
    # 查询数据库中是否已经存在相同主键值的记录
    query = text("SELECT * FROM jd_bill WHERE 运输任务号 = :primary_key")
    query = query.bindparams(primary_key=primary_key_value)
    
    try:
        result = connection.execute(query)
        existing_data = result.fetchall()

        if not existing_data:
            print(index)
            row.to_sql(name='jd_bill', con=mydb, if_exists='append', index=False)
    except Exception as e:
        messagebox.showerror("错误1", f"数据库连接失败: {str(e)}")    
    finally:
        connection.close()

# 关闭数据库连接
engine.dispose()

print("数据导入成功！")
SystemExit()