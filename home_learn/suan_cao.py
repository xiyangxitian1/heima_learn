import random
import time

list = [1, 3, 6, 4, 5, 7, 9]
result = 10
len1 = len(list)
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
    l = [list[i] for i in index_list]  # 列表推导式
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
