class Dog:
    def t1(self):
        print('abc')

    @staticmethod
    def t2():
        print('222')


if __name__ == '__main__':
    d = Dog()
    d.t1()
    d.t2()
    Dog.t2()
    Dog.t1()  # 缺少参数

