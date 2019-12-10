import functools
import my_util
a = [1, 2, 3]
b = functools.reduce(lambda x, y: x + y, a)
print(b)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 列出列表中的偶数
b = filter(lambda x: x % 2 == 0, a)
print(list(b))
