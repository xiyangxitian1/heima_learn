# zip
# l = [(1, 2, 3, 4, 5), ('a', 'b', 'c', 'd')]
# l = [[1, 2, 3, ], [4, 5, 6]]  #  说明元组和数组都是可以的
# a = zip(*l)
# l = [(1, 4, 7), (2, 5,), (3, 6, 7)]  # 还可以用多个参数直接来接收
# a, b = zip(*l)
# print(a)
# print(b)
# a, b = map(lambda x, y, z: (x, y + 1, z + 2), (1, 4, 7), (2, 5,), (3, 6, 7))
# print(a, b)

#
# a = zip(*l)
# # a = zip(*a)
# result = []
# for a1 in a:
#     result.append(a1)
# #
# print(result)

# map
# map()函数不改变原有的 list，而是返回一个新的 list。
# 1.
# def fun(x):
#     return x * x
#
# list = [1, 2, 3, 4, 5, 6]
# list1 = map(fun, list)
# for l in list1:
#     print(l)

# 2.
# l2 = map(lambda x, y: x ** y, [1, 2, 3], [1, 2, 3])
# for i in l2:
#     print(i)
# 3.
# l3 = map(lambda x, y: (x ** y, x + y), [1, 2, 3], [1, 2, 3])
# for i in l3:
#     print(i)
# 4.python3中可以处理类表长度不一致的情况，但无法处理类型不一致的情况，
#  从结果看和zip一样,过长的就去不计算了,以最短的为准
# l4 = map(lambda x, y: (x ** y, x + y), [1, 2, 3], [1, 2])
# for i in l4:
#     print(i)
# 下面这种类型不一致的就无法处理,这也是正常的,如果 类型不一样的超出长度就算是舍弃了,也可以处理
# l4 = map(lambda x, y: (x ** y, x + y), [1, 2, 3], [1, 2, 'a'])
# for i in l4:
#     print(i)
# 5.

# 特殊用法，做类型转换： 自动的把1234这个字符串处理成一个列表了 [1,2,3,4]
# l = map(int, list('1234'))
# # l = map(int, ['1', '2', '3', '4'])
# for i in l:
#     print(type(i))
#     print(i)

#
# 如果函数是 None，自动假定一个‘identity’函数,这时候就是模仿 zip()函数，
# l = [1, 2, 3]
# x = map(None, l)
# print(x == None)
# print(x)
# print(type(x))
# for i in x:
#     print(i)
# 这时候 None 类型不是一个可以调用的对象。所以他没法返回值。
# 目的是将多个列表相同位置的元素归并到一个元组。如：

# >>> print map(None, [2,4,6],[3,2,1])
# [(2, 3), (4, 2), (6, 1)]
# 但是在 python3中，返回是一个迭代器，所以它其实是不可调用的
