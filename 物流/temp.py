a = '300'
b = '200'
c = '100'

# 创建一个列表来保存where语句的条件
where_clause_list = []

# 循环遍历三个变量
for i in range(3):
    # 如果变量的值不为空，那么将其加入到where条件列表中
    if a != "":
        where_clause_list.append("a = '%s'" % a)
        break
    if b != "":
        where_clause_list.append("b = '%s'" % b)
        break
    if c != "":
        where_clause_list.append("c = '%s'" % c)
        break
print(where_clause_list)
# 将where条件列表转换为字符串
where_clause = " AND ".join(where_clause_list)

# 输出where语句
print(where_clause)