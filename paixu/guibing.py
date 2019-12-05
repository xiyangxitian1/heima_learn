from datetime import datetime
from random import randint


def mergingSort(arr):
    """归并排序"""
    if arr == None or len(arr) < 2:
        return arr
    num = len(arr) >> 1
    leftArr = arr[:num]
    rightArr = arr[num:]
    # print("split lef: " + str(leftArr) + " right: " + str(rightArr))
    return mergingArr(mergingSort(leftArr), mergingSort(rightArr))


def mergingArr(arr1, arr2):
    """归并列表"""
    i, j, k = 0, 0, 0
    # result = [0 for i in range(len(arr1) + len(arr2))]
    result = [0] * (len(arr1) + len(arr2))
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result[k] = arr1[i]
            i += 1
        else:
            result[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):
        result[k] = arr1[i]
        k += 1
        i += 1
    while j < len(arr2):
        result[k] = arr2[j]
        k += 1
        j += 1
    return result


lst = [randint(1, 1000000) for i in range(1000000)]
start = datetime.now()
mergingSort(lst)
end = datetime.now()
s = (end - start).seconds
print("use time is {}s".format(s))  # 8s
