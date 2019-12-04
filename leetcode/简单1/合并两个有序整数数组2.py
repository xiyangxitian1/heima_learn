from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sum_num = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                sum_num.append(nums1[i])
                i += 1
            else:
                sum_num.append(nums2[j])
                j += 1
        if i == m:
            print(nums1)
            print(sum_num)
            print(nums2)
            # nums1[:] = sum_num + nums2[j:]  # 为什么直接写nums1 = 就不可以呢。而要这样才行
            # nums1 = sum_num + nums2[j:]  #  自己测试感觉是一样的
        else:
            nums1[:] = sum_num = nums1[i:]
        print(nums1)


if __name__ == '__main__':
    a = [1, 2, 3, 0, 0, 0]
    b = 3
    c = [2, 5, 6]
    d = 3
    Solution().merge(a, b, c, d)
