def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum1(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        print(i, num)
        # print(hashmap.get(target - num))
        if hashmap.get(target - num) is not None:
            return [i, hashmap.get(target - num)]
        hashmap[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况
        print(hashmap)


l = [2, 2, 4, 3, 1]
target = 4
result = twoSum1(l, target)
print(result)
# hashmap = {0: 1}
# print(hashmap.get(0))
