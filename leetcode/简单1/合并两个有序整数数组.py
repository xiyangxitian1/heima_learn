from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums11 = nums1
        if not nums2:
            return nums11[:m]
        if not nums11:
            return nums2[:n]

        i, j = 0, 0
        end = m
        while j < n:
            if nums11[i] > nums2[j]:
                nums11.insert(i, nums2[j])
                j += 1
                end += 1
            i += 1
            if i == end:
                nums11 = nums11[:end] + nums2[j:]
                break
        if len(nums11) > m + n:
            nums11 = nums11[:m + n]
        nums1 = nums11
        print(nums1)



if __name__ == '__main__':
    a = [1, 2, 3, 0, 0, 0]
    b = 3
    c = [2, 5, 6]
    d = 3
    Solution().merge(a, b, c, d)
