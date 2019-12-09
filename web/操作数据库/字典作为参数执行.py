import pymysql

# 192.168.84.128

conn = pymysql.connect(host='192.168.84.128', user='root', passwd='mysql', db='tt', charset='utf8')
cs = conn.cursor()
row = cs.execute('insert into students(name,age) values (%(name)s,%(age)s)', {'age': 13, 'name': '王霸天'})
print(row)
cs.close()
conn.commit()
conn.close()
