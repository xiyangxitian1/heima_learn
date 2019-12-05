from random import randint
from datetime import datetime


def quick_sort(arr):
    sort(arr, 0, len(arr) - 1)


def sort(arr, start, end):
    """快速排序"""
    # print("left is {} end is {}".format(start, end))
    if start >= end:
        return
    left = start
    right = end
    # baseNum = arr[0]
    while left < right:
        while left < right and arr[right] >= arr[left]:
            right -= 1
        if left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            # print(arr)

        while left < right and arr[left] <= arr[right]:
            left += 1
        if left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            right -= 1
            # print(arr)

    if left > start:
        sort(arr, start, left - 1)
    if right < end:
        sort(arr, right + 1, end)


# lst = [1, 4, 5, 7, 3, 2]
# sort(lst, start=0, end=len(lst) - 1)
# print("最终结果:{}".format(lst))

lst = [randint(1, 1000000) for i in range(1000000)]
start = datetime.now()
quick_sort(lst)
end = datetime.now()
s = (end - start).seconds
print("use time is {}s".format(s))  # 5s
