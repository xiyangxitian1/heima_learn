import pymysql

# host=None, user=None, password="",
# database=None, port=0, unix_socket=None,
# charset='', sql_mode=None,
# read_default_file=None, conv=None, use_unicode=None,
# client_flag=0, cursorclass=Cursor, init_command=None,
# connect_timeout=10, ssl=None, read_default_group=None,
# compress=None, named_pipe=None,
# autocommit=False, db=None,
conn = pymysql.connect(host='192.168.84.128', port=3306, charset='utf8', db='tt', user='root', password='mysql')
cs = conn.cursor()
cs.execute('select * from students')
data = cs.fetchone()
print('data', data)
cs.close()
conn.close()
