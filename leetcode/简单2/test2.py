list1 = [1, 2, 3, 4, 5]
# 得到[4,3,2,1]
# list2 = list1[:-1]
# list2.reverse()
list2 = list1[:]
list2.append(6)
# list2.reverse()
print(list2)
print(list1)