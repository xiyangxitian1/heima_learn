from pymysql.connections import Connection

# def __init__(self, host=None, user=None, password="",
#              database=None, port=0, unix_socket=None,
#              charset='', sql_mode=None,
#              read_default_file=None, conv=None, use_unicode=None,
#              client_flag=0, cursorclass=Cursor, init_command=None,
#              connect_timeout=10, ssl=None, read_default_group=None,
#              compress=None, named_pipe=None,
#              autocommit=False, db=None, passwd=None, local_infile=False,
#              max_allowed_packet=16*1024*1024, defer_connect=False,
#              auth_plugin_map=None, read_timeout=None, write_timeout=None,
#              bind_address=None, binary_prefix=False, program_name=None,
#              server_public_key=None):
conn = Connection(host='192.168.84.128', passwd='mysql', charset='utf8', user='root', db='tt', autocommit=True)
conn.connect()
cs = conn.cursor()
# conn.begin()
while 1:
    student_name = input('请输入要查询的学生姓名：')
    # if not my_id.isdigit():  这样也把sql注入给
    #     continue
    if student_name == '0':
        break
    # row = cs.execute('select * from students where name = "%s" ' % student_name)  # " or 1=1 or 1 = " sql注入
    # row = cs.execute('select * from students where name = "" or 1=1 or 1 = "" or name = %s ',[student_name])  # " or 1=1 or 1 = " sql注入
    row = cs.execute('select * from students where name = %s ', [student_name])
    # conn.commit()
    # conn.rollback()
    print('影响或查询的行数', row)
    data = cs.fetchall()
    print(data)

cs.close()
conn.close()
