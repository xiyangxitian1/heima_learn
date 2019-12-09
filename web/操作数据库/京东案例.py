import pymysql


class JDServer(object):
    # 连接虚拟机中的mysql 192.168.84.128

    def __init__(self, host, db, user, pwd):
        self.conn = pymysql.connect(host=host, db=db, user=user, port=3306, passwd=pwd, charset='utf8')
        self.dict = {'1': self.__fetch_all_info, '2': self.__fetch_cate_of_goods, '3': self.__add_new_cate,
                     '4': self.__update_price, '5': self.__update_cate, '6': self.__fetch_info_with_id,
                     '7': self.__fetch_info_with_id_safe}

    def __del__(self):
        # 对象销毁的时候释放连接
        print('释放连接……')
        self.conn.close()

    # 显示菜单方法
    def __print_menu(self):
        print('1. 查询所有商品信息')
        print("2. 查询所有包含商品的分类")
        print("3. 添加新商品分类")
        print("4. 将所有商品价格加1000")
        print("5. 将所有笔记本的分类改为超级本")
        print("6. 根据id查询商品信息")
        print("7. 根据id查询商品信息安全方式")
        print("8. 退出系统")

    # 打印结果方法
    def __show_query_result(self, result):
        for data in result:
            print(data)

    # 服务器运行方法,实现主体逻辑
    def run(self):
        while 1:
            self.__print_menu()
            num = input('请输入要进行的操作：').strip()  # 用户可以不小心多办理了空格，所以要应对一下
            if num == '8':
                break
            elif num not in self.dict.keys():
                print('你输入的有误请重新输入：')
            else:
                # 执行相应的操作
                self.dict[num]()

    def __querySql(self, sql, params=None):
        cs = self.conn.cursor()
        cs.execute(sql, params)
        data = cs.fetchall()
        # cs.fetchmany(5)
        cs.close()
        return data

    def __updateSql(self, sql, params=None):
        cs = self.conn.cursor()
        row = cs.execute(sql, params)
        self.conn.commit()
        cs.close()
        print('影响的行数:', row)
        return row

    # 1. 查询所有商品信息
    def __fetch_all_info(self):
        data = self.__querySql('select * from goods')
        self.__show_query_result(data)

    # 2. 查询所有包含商品的分类
    def __fetch_cate_of_goods(self):
        data = self.__querySql('select distinct g1.* from good_cates g1 inner join goods g2 on g1.id = g2.cate_id')
        self.__show_query_result(data)

    # 3. 添加商品分类
    def __add_new_cate(self):
        name = input('请输入要插入商品的各类名：')
        sql = 'insert into good_cates(name) values (%s)'
        self.__updateSql(sql, [name])

    # 4. 将所有商品价格加1000
    def __update_price(self):
        self.__updateSql('update goods set price = price+1000 ')

    # 5. 将所有笔记本的分类改为超级本
    def __update_cate(self):
        sql = 'update goods set cate_id = (select id from good_cates where name = "超级本") where cate_id = (select id from good_cates where name = "笔记本")'
        self.__updateSql(sql)

    # 6. 根据id查询商品信息
    def __fetch_info_with_id(self):
        """特意来写一个会发生sql注入的查询"""
        cs = self.conn.cursor()
        id = input('请输入商品编号：')
        cs.execute('select * from goods where id = %s ' % id)
        data = cs.fetchmany(10)  # 最多可以查询出10条数据
        for d in data:
            print(d)
        cs.close()

    # 7. 根据id查询商品信息安全方式
    def __fetch_info_with_id_safe(self):
        id = input('请输入商品编号：')
        data = self.__querySql('select * from goods where id = %(id)s ', {"id": id})  # 查询会把参数列表里的数字给转换成字符串
        self.__show_query_result(data)


def main():
    # 创建服务器对象,并传入相应参数

    config = {
        'host': '192.168.84.128',
        # 'port': 3306,
        'user': 'root',
        'pwd': 'mysql',
        'db': 'jing_dong',
        # 'charset': 'utf8'
    }
    jd = JDServer(**config)
    # 1/0  测试在发生意外时会不会释放连接  证明是可以的
    # 启动服务器
    jd.run()


if __name__ == '__main__':
    main()
