class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        nums.append(target)
        nums.sort()
        return nums.index(target)
        # return None if nums.append(target) else nums.index(target) if not nums.sort() else None


if __name__ == '__main__':
    x = [1, 3, 5, 6]
    y = 2
    print(Solution().searchInsert(x, y))
