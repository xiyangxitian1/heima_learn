import random
import time

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
len1 = len(list1)
# print(list)
# list.sort()

result_list = []
index_list = []
count = 0
while True:
    # index_list.clear()
    index = random.randint(0, len1 - 1)
    if index not in index_list:
        index_list.append(index)
    else:
        continue

    # print('index_list', index_list)
    l = [list1[i] for i in index_list]  # 列表推导式                 
    l.sort()
    sum1 = sum(l)
    if sum1 == result:
        if l not in result_list:
            count = 0
            print('结果是:', l)
            result_list.append(l)
            index_list.clear()
            continue
        else:
            count += 1

    if len(index_list) == len1:
        # print('clear..')
        index_list.clear()

    if count > 2:
        print('已经查找全部结果')
        break

print('结果是:')
for res in result_list:
    print(res)
