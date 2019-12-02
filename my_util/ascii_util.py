# from http import  server
import random


# print(ord('a'))  # 97
# print(ord('z'))  # 122
#
# print(ord('A'))  # 65
# print(ord('Z'))  # 90
#
# print(ord('0'))  # 48
# print(ord('1'))  # 49
# print(ord('9'))  # 57
#
# print(chr(97))  # a
# print(ord(1))
# print(ord(9))
def getOne() -> str:
    # 随机获取 a-zA-Z0-9中的一个
    # l = list(range(97, 123)) + list(range(65, 91)) + list(range(48, 58))
    l = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
         120, 121, 122, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
         89, 90, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

    # return chr(l[random.randint(0, len(l) - 1)])
    return chr(l[random.randint(0, 61)])


def getN(n):
    # 随机获取n个a-zA-Z0-9 并组合成字符串返回
    result = ''
    for _ in range(n):
        result += getOne()
    return result

# 设置成私有方法，不让外部调用
def __getAll(n) -> list:
    f = open('f:/8pwd.txt', 'w')
    l = []
    count = 0  # 计数，如果超过次数就退出
    while count < 10:
        s = getN(n)
        if s not in l:
            count = 0
            l.append(s)
            f.write(s + '\n')
        else:
            count += 1
    f.close()
    return l


def getMN(m, n) -> list:
    # 获取M个长度为N的字符串 并且不能重复，如果不够M个就全部返回
    l = []
    count = 0  # 计数，如果超过次数就退出
    while len(l) < m:
        s = getN(n)
        if s not in l:
            count = 0
            l.append(s)
        else:
            count += 1
            if count > 5:
                break

    return l


if __name__ == '__main__':
    # print(getMN(100, 10))
    # l = getMN(100000, 6)  # 10万长度为6的
    # f = open('pwd.txt', 'w')
    # # 依次保存长度为6到10的密码 每个长度的密码保存100000个
    # for n in range(6, 11):
    #     for pwd in getMN(100000, n):
    #         f.write(pwd + '\n')
    #         f.flush()
    # f.close()

    l = __getAll(8)
    if '3pn9tse6' in l:
        print('ok')
    else:
        print('no')
