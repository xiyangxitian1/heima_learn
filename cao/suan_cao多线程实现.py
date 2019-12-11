import time
import threading
import random


def getResult(list1, result, count_num, max_ji_count=10000000):
    """

    :param list1:        原始列表
    :param result:      想要的结果
    :param count_num:  结果列表含有的元素个数
    :param max_ji_count: 默认循环一千万次还没有找到结果就认为没有结果
    :return:
    """
    len1 = len(list1)
    result_list = []
    count = 0
    ji_count = 0  # 计算次数  默认循环一千万次还没有找到结果就认为没有结果
    while True:
        index_set = set()  # 因为set不会重复，所以使用set集合，这是一个随机的索引集合
        while len(index_set) < count_num:
            index_set.add(random.randint(0, len1 - 1))
        result_set = {list1[i] for i in index_set}
        sum1 = sum(result_set)
        if sum1 == result:
            if result_set not in result_list:
                count = 0
                print('结果是:', result_set)
                result_list.append(result_set)
                ji_count = 0
                continue
            else:
                count += 1
        if ji_count > max_ji_count:
            print("已经找出了所有结果")
            break
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
    for r in list1:
        if r == result:
            print("结果是:", r)

    for i in range(2, len(list1)):  # 还是不适合多线程
        threading.Thread(target=getResult, args=(list1, result, i)).start()
