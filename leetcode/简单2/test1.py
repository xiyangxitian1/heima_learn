# list1 = [1, 2, 3, 4]
# print(type(reversed(list1)))
# print()
from my_util.time_util import get_time

list1 = list(range(10000000))


@get_time
def f1():
    list1.reverse()
    print(len(list1))


@get_time
def f2():
    list2 = reversed(list1)
    list(list2)


@get_time
def f3():
    list2 = list1[::-1]
    print(len(list2))

@get_time
def f4():
    list2 = list1[:]

if __name__ == '__main__':
    f1()
    f2()
    f3()
    f4()