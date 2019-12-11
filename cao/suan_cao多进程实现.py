import time
import multiprocessing
import random


def getResult(list1, result):
    len1 = len(list1)
    # print(list)
    # list.sort()
    result_list = []
    count = 0
    while True:
        # index_list.clear()
        count_num = random.randint(2, len1 - 1)  # 随机生成一个数 num
        # 随机生成一个长度为count_num的列表
        # l = [list1[i] for i in index_list]  # 列表推导式
        # 生成count_num个不重复的索引，然后再生成列表
        index_set = set()  # 因为set不会重复，所以使用set集合
        while len(index_set) < count_num:
            index_set.add(random.randint(0, len1 - 1))

        # l = [list1[random.randint(0, len1 - 1)] for _ in range(count_num)]  # 这样生成的数会有重复，不行
        l = [list1[i] for i in index_set]
        l.sort()
        sum1 = sum(l)
        if sum1 == result:
            if l not in result_list:
                count = 0
                print('结果是:', l)
                result_list.append(l)
                continue
            else:
                count += 1

    return result_list


if __name__ == '__main__':
    list1 = [
        -11048.44,
        3.25,
        18.19,
        74.57,
        82.77,
        118.09,
        304.05,
        623.05,
        641.14,
        716.39,
        761.93,
        930.23,
        1154.23,
        1216.83,
        1419.63,
        1876.93,
        2514.38,
        2581.96,
        3000,
        3151.25,
        5824.94,
        6452.4,
        8825.27,
        10553.48,
        10557.93,
        11524.95,
        13983.14,
        17203.12,
        20652.37,
        23711.04,
        48582.71,
        55850.48,
        55920.31,
        62647.44,
        65431.46,
        72519.35,
    ]
    # list = [1, 3, 6, 4, 5, 7, 9]
    result = 285718.69
    if sum(list1) == result:
        print("整个数据就是一个正确的结果!")
    # 开启5个进程  (进程特别消耗资源，少开点)
    for _ in range(5):
        multiprocessing.Process(target=getResult, args=(list1, result)).start()
