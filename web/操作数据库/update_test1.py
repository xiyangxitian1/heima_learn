import pymysql
#
# (self, host=None, user=None, password="",
# database=None, port=0, unix_socket=None,
# charset='', sql_mode=None,
# read_default_file=None, conv=None, use_unicode=None,
# client_flag=0, cursorclass=Cursor, init_command=None,
# connect_timeout=10, ssl=None, read_default_group=None,
# compress=None, named_pipe=None,
# autocommit=False, db=None, passwd=None, local_infile=False,
# max_allowed_packet=16*1024*1024, defer_connect=False,
# auth_plugin_map=None, read_timeout=None, write_timeout=None,
# bind_address=None, binary_prefix=False, program_name=None,
# server_public_key=None):
conn = pymysql.connect(host='192.168.84.128', charset='utf8', db='tt', user='root', passwd='mysql',
                       autocommit=True)
# if db is not None and database is None:
#     database = db
# if passwd is not None and not password:
#     password = passwd

# 看到源码中有上面这一句，所以database不写，写上db也会是一样的效果,同理passwd
# 经过看源码得出port 不写默认也会给用3306,host不写默认是localhost,密码不写默认是 空""
# 可以设置成自动提交 autocommit=True 就可以自动提交了，
cs = conn.cursor()
row = cs.execute('update students set age = 24 where id = 16')
# data = cs.fetchone()
print('影响的行数：', row)
# conn.commit()
cs.close()
conn.close()
