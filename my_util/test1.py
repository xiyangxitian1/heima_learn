# a = "ab\ncde\ncf heLLao"
# print(a[:])
# print(a[::])
# print(a[::2])
# print(a[5:1:-2])
# print(a[-1::-1])
# b = a.find('cd', 2, -100)
# print(b)
# c = a.index('cd')
# print(c)
# print(a.count('cd'))
#
# print(a.split('c',2))
# print(a.capitalize())
# print(a.title())
# print(a.upper())
# print(a.upper().isupper())
# print(a.ljust(30,'L'))
# print(a.rjust(30,'0'))
# print(a.center(30))
# print(a.rfind('a'))
# print(a.rfind('o342'))
# print(a.find('a'))
# print(a.partition('c'))

# print(a.splitlines())
# a='abcd'
# print(a.isalpha())
# print(a.isascii())
# a= '1234'
# print(a.isalnum())
# a = 'a b c  d       e f g '
# print(a.split())
# a = [1, 2]
# b = [3, 4]
# print(a.append(b))
# a.extend(b)
# print(a)
# from my_util.time_util import get_time
# a = list(range(1000000))
# b = list(range(1000000))
# @get_time
# def f1():
#     a.extend(b)
#
# @get_time
# def f2():
#     c = a + b
#
# f1()
# f2()

# a = [1, 2, 3, 4, 0, 7, 6]
# a.sort(key=lambda x: 0 - x)
# print(a)
# a = (1, 2, 3, 4, 5)
# # del a[2]
# a[2]=3
a = {1: 'a', 2: 'b'}
# b = a.get(0, 3)  # 根据键来查找，如果没有返回默认值3，如果不设置默认值，找不到会返回None
# print(b)
# print(len(a))
# a.clear()
# print(a)
# for i in a.items():
#     print(i)
# for i, v in enumerate(a.items()):
#     print(i, v)
# a = [3, 4, 5, 6]
# dict = {}
#
# for i, v in enumerate(a):
#     dict[i] = v
#
# print(dict)
# dict1 = dict.copy()
# del dict[1]
# print(dict1)
# a = [1, 2, 3, 4]
# d = tuple(a)
#
# 实现了列表转为字典
# d = dict(enumerate(a))
# print(d)
# # 字典转为列表，会舍弃key或values  也可以用两个列表来装
# l1 = list(d.values())
# print(l1)
# 以前字典是无序的，存放的顺序和取出的顺序并不一致，所以要有有序字典来OrderDict
# 在Python3.6以后，字典实现了有序，并且占用的空间更少了。
# b = a * 4  # 乘用在列表、字符串、元组 上代表的是复制
# print(b)
import operator

# 注意pyhon3已经没有cmp这个函数了，不过用 operator来代替使用
# lt(a,b) 相当于 a<b     从第一个数字或字母（ASCII）比大小
#
# le(a,b)相当于a<=b
#
# eq(a,b)相当于a==b     字母完全一样，返回True,
#
# ne(a,b)相当于a!=b
#
# gt(a,b)相当于a>b
#
# ge(a,b)相当于 a>=b
# a = {'age': 18}
# b = {'age': 19}

# a = operator.pow(2,4)
# print(a)
print("                            _ooOoo_  ")
print("                           o8888888o  ")
print("                           88  .  88  ")
print("                           (| -_- |)  ")
print("                            O\\ = /O  ")
print("                        ____/`---'\\____  ")
print("                      .   ' \\| |// `.  ")
print("                       / \\||| : |||// \\  ")
print("                     / _||||| -:- |||||- \\  ")
print("                       | | \\\\\\ - /// | |  ")
print("                     | \\_| ''\\---/'' | |  ")
print("                      \\ .-\\__ `-` ___/-. /  ")
print("                   ___`. .' /--.--\\ `. . __  ")
print("                ."" '< `.___\\_<|>_/___.' >'"".  ")
print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
print("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
print("                            `=---='  ")
print("  ")
print("         .............................................  ")
print("                  佛祖镇楼                  BUG辟易  ")
print("          佛曰:  ")
print("                  写字楼里写字间，写字间里程序员；  ")
print("                  程序人员写程序，又拿程序换酒钱。  ")
print("                  酒醒只在网上坐，酒醉还来网下眠；  ")
print("                  酒醉酒醒日复日，网上网下年复年。  ")
print("                  但愿老死电脑间，不愿鞠躬老板前；  ")
print("                  奔驰宝马贵者趣，公交自行程序员。  ")
print("                  别人笑我忒疯癫，我笑自己命太贱；  ")
print("                  不见满街漂亮妹，哪个归得程序员？")