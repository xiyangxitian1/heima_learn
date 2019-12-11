def f1(name):
    def say(msg):
        nonlocal name  # 用nonlocal关键字修改外部函数的变量
        name = '王五'
        # global
        print(name, msg)

    return say


a = f1('张三')

a("上学去")

# del a    销毁
a("不去")
