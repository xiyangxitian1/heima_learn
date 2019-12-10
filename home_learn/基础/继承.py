class Animal(object):

    def __init__(self):
        print("Animal init....")

    def eat(self):
        print("Animail eat...")


class Dog(Animal):

    def __init__(self):
        print("Dog .. init ... ")

    def eat(self):
        print("Dog.eat....")


class Dog1(Animal):

    def __init__(self):
        print("Dog1 .. init ...")

    def eat(self):
        print("Dog 1 eat ....")


class XTQ(Dog, Dog1):

    def __init__(self):
        pass
        # super(XTQ, self).__init__()
        # super(Dog, self).__init__()
        # super(Dog1, self).__init__()
        # Dog.eat(object())
        # super(Dog, self).eat()

    def eat(self):
        print("XTQ .. eat...")


if __name__ == '__main__':
    # xtq = XTQ()
    # xtq.eat()
    # 调用xtq 的eat方法
    XTQ().eat()
    # 调用 Dog的eat
    # super(XTQ, XTQ()).eat()
    # Dog.eat(Dog())
    Dog().eat()
    # 调用 Dog1的eat
    # Dog1.eat(Dog1())
    Dog1().eat()
    # 调用 Animail的eat
    # super(Dog, Dog()).eat()
    # super(Dog1, Dog1()).eat()
    Animal().eat()
