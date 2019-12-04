import keyword  # 关键字
import dis  # 程序执行


# print(keyword.kwlist)
#
# # 所以True为1 False为0
# a = True + True
# b = False + True
#
# # if 0: == if False:
# #
# print(int(True))
# print(int(False))
#  在python3以下的版本中     while True: 是要比while 1慢的 python3的时候True和False成了关键字，速度就一样了
# while a is True 没 没有 while a 快  while a 与 while not a 是一样快的。 所以能不用is就别用了。
# 当然 if也是一样，所以能不加is就别加了

def a():
    i = 1
    i += 1


def b():
    i = 1
    i = i + 1


dis.dis(a)
print("*" * 100)
dis.dis(b)
