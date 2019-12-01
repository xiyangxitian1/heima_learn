class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        不使用额外的空间删除有序数组中的重复项
        利用下有序这个条件
        """
        if len(nums) < 2:
            print(nums)
            return len(nums)
        i = 0
        len1 = len(nums) - 1
        while i < len1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
                len1 -= 1
            else:
                i += 1
        print(nums)
        return len(nums)


if __name__ == '__main__':
    x = [1, 2, 2, 3, 3, 4]
    x = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    x = [1, 1]
    print(Solution().removeDuplicates(x))
