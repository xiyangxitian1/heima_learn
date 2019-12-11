from pymysql.connections import Connection
import time

conn = Connection(host='192.168.84.128', passwd='mysql', charset='utf8', user='root', db='tt', autocommit=True)
conn.connect()

while 1:
    cs = conn.cursor()
    row = cs.execute('select * from students where id = %s ', [18])
    print("row", row)
    # conn.commit()
    time.sleep(2)
    data = cs.fetchone()  # 每次取1条数据
    print(data)
    cs.close()

conn.close()
