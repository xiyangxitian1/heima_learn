# a, b = [1, 2]
# print(a, b)

# 交换两个变量的值
# 1.定义一个中间变量
# c = a
# a = b
# b = c
# print(a, b)

# 2.用加减法
# a = a + b
# b = a - b  # 现在b已经是原来的a的值了
# a = a - b  # ok
# print(a, b)


# 3. 用异或运算    相同为0，  0和a异或还是a
# a = a ^ b
# b = a ^ b    # b现在是a的值了
# a = a ^ b    # ok
# print(a, b)

# 4. python自带的赋值运算
# a, b = b, a
# print(a, b)

#############################################################
# def test1(b):  # 变量b一定是一个局部变量，就看它指向的是谁？可变还是不可变
#     b += b  # += 是直接对b指向的空间进行修改,而不是让b指向一个新的
#     # b = b+b  # xx = xx+yyy 先把=号右边的结果计算出来,然后让b指向这个新的地方,不管原来b指向谁
#     # 现在b一定指向这个新的地方
#     print(id(b))  # 可以看这个id是不是一样的，一样的就会和外面的一起改变，因为修改了相同地址里的值。
#
#
# # a = [11, 22]
# a = 100
# print(id(a))
# test1(a)
# print(a)

# def test():
#     print('test...')
#
# test()
#
# def test(a, b):
#     print('test2....')
#
#
# test(1, 2)

# f1 = lambda:print('a')
# f1()

# list1 = [x for x in range(10) if x % 2 == 0]
# print(list1)
# 请写出一段 Python 代码实现分组一个 list 里面的元素,
# #比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]
# 方法一：
# list1 = list(range(1, 101))
# list2 = []
# while list1:
#     list2.append(list1[:3])
#     list1 = list1[3:]
# print(list2)

# 方法二：
# list2 = [[x - 2, x - 1, x] for x in list1 if x % 3 == 0] + [[100]]
# print(list2)

# 方法三：
a = [x for x in range(1, 101)]
b = [a[x:x + 3] for x in range(0, len(a), 3)]
print(b)
