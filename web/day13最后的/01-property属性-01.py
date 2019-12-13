class Person(object):

    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

# class Person(object):
#
#     def __init__(self):
#         self.__age = 0
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         self.__age = age[0]
#
#     age = property(get_age, set_age)
#
#
# if __name__ == '__main__':
#     p1 = Person()
#     print(p1.age)
#     p1.age = (40,)
#     print(p1.age)
#
if __name__ == '__main__':
    p1 = Person()
    print(p1.age)
    p1.age = 30
    print(p1.age)
