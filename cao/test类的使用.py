class Dog(object):

    def __init__(self):
        # super().__init__()
        print("Dog....")

    def eat(self):
        print("Dog eat...")


class Animal(object):

    def __init__(self):
        print("Animal...")

    def eat(self):
        print("Animal .. eat...")


class JinMao(Animal, Dog):

    def __init__(self):
        pass
        # super(Dog, self).__init__()
        # super(Animal, self).__init__()
        # print("JinMao init...")

    def eat(self):
        super(Animal, self).eat()


if __name__ == '__main__':
    jinMao = JinMao()
    jinMao.eat()
