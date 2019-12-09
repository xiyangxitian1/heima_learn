from my_util.time_util import get_time

import copy


# list1 = list(range(100000000))


@get_time
def f1():
    list2 = copy.copy(list1)  # 这种复制和切片的速度差不多快
    print(len(list2))


@get_time
def f2():
    list2 = list1[:]
    print(len(list2))


@get_time
def f3():
    list2 = copy.deepcopy(list1)
    print(len(list2))



# 可以看到浅拷贝只是对第一层的元素进行了拷贝，但是如果元素是列表的话，那么修改也会跟着改变，切片也是浅拷贝
# 使用的时候要注意在元素都是单个类型如整型，的时候 使用，而列表 不行。
list1 = [1, 2, 3, 4, ['a', 'b', 'c']]
list2 = copy.copy(list1)
list3 = copy.deepcopy(list1)
list1[-1].append('d')
print(list1)
print(list2)
print(list3)
