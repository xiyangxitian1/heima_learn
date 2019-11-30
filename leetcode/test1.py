class Solution(object):

    def mergelist(self, nums1, nums2):
        """两个数组都是有序的时候进行合并"""
        begin = 0
        for n1 in nums1:
            for i in range(begin, len(nums2)):
                if n1 < nums2[i]:
                    nums2.insert(i, n1)
                    begin = i + 1
                    break
                elif i == len(nums2) - 1:
                    begin = len(nums2)
                    nums2.insert(len(nums2), n1)
                    break
        return nums2

    def return_half_nums(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) % 2 == 0:
            len1 = len(nums) // 2
            return (nums[len1] + nums[len1 - 1]) / 2
        else:
            return nums[len(nums) // 2]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            print('数据全部为空')
            return
        # nums2是空的情况 ，交换两个列表，让nums1为空
        if not nums2:
            nums2 = nums1
            nums1 = []

        # nums1是空的情况
        if not nums1:
            return self.return_half_nums(nums2)

        # 数据全不为空的情况
        nums = []
        if nums1[-1] < nums2[0]:
            nums = nums1 + nums2
        elif nums1[0] > nums2[-1]:
            nums = nums2 + nums1
        if nums:
            return self.return_half_nums(nums)

        # 组合 nums1 与 nums2
        # 插入排序会不会很好。因为都是有序的

        nums = self.mergelist(nums1, nums2)
        print(nums)
        return self.return_half_nums(nums)


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    # 1,1,2,2,3  预期是2  返回的却是1.5
    r = s.findMedianSortedArrays(nums1, nums2)
    print(r)
