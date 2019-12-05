from datetime import datetime
from random import randint


def sort(arr):
    """插入排序"""
    length = len(arr)
    for i in range(1, length):
        temp = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] > temp:
                arr[j + 1] = arr[j]
            else:
                break
        arr[j + 1] = temp


def insertsort(arr):
    """插入排序"""
    length = len(arr)
    for i in range(1, length):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


#
arr = [1, 3, 2, 9, 8, 7, 5, 6]
insertsort(arr)
print(arr)
# lst = [randint(1, 1000000) for i in range(10000)]
# start = datetime.now()
# sort(lst)
# end = datetime.now()
# s = (end - start).seconds
# print("use time is {}s".format(s))  # 3s
