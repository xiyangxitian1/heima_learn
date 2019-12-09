import pymysql

# 创建连接对象
conn = pymysql.connect(host='192.168.84.128', port=3306, user='root', password='mysql', database='tt', charset='utf8')

# 获取游标对象
cursor = conn.cursor()

try:
    # 添加 SQL 语句
    # sql = "insert into students(name) values('刘璐'), ('王美丽');"
    # 删除 SQ L语句
    # sql = "delete from students where id = 5;"
    # 修改 SQL 语句
    sql = "update students set name = '王铁蛋' where id = 6;"
    # 执行 SQL 语句
    row_count = cursor.execute(sql)
    print("SQL 语句执行影响的行数%d" % row_count)
    # 提交数据到数据库
    conn.commit()
except Exception as e:
    # 回滚数据， 即撤销刚刚的SQL语句操作
    conn.rollback()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()
