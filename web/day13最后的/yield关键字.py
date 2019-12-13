# def foo(n):
#     print("foo..")
#     for i in range(n):
#         print("生成数据0000")
#         yield i
#         print("生成数据1111")
#
#
# if __name__ == '__main__':
#     g1 = foo(2)
#     for a in g1:
#         pass

# 31 的阶乘 就算是只是遍历，也用太久的时间了 8222 8386541779 2281772556 2880000000
# sum1 = 1
# for i in range(2, 32):
#     sum1 *= i
# print(sum1)

# l1 = (i for i in range(30000000000000000000000000000000))
# print("结束")
# for i in l1:
#     pass
# print("总结束")

# import copy
#
# a = (1, [3, 4])
# b = copy.deepcopy(a)
# print(id(a[0]))
# print(id(b[0]))