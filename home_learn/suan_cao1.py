import random
import time


def suanSum(list1, target):
    list1.sort()
    begin = 0
    end = 1

    for i in range(len(list1)):
        for j in range(i + 1, len(list1) + 1):
            if sum(list1[i:j]) == target:
                print(list1[i:j])


if __name__ == '__main__':
    x = [1, 3, 6, 4, 5, 7, 9]
    # 1,3,4,5,6,7,9  所以没有等于10的，但是 列表中是有和是10的，所以这个算法不可以
    # 那达到所有的排序再调用这个方法？  那就太慢了，因为所有的排序也是太多了。

    target = 10
    suanSum(x, target)
