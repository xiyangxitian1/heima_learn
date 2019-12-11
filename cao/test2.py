from my_util.time_util import get_time
from copy import copy
list1 = list(range(100000000))
@get_time
def foo1():
    list1.copy()

@get_time
def foo2():
    list1[:]

@get_time
def foo3():
    copy(list1)

if __name__ == '__main__':
    foo1()
    foo2()
    foo3()