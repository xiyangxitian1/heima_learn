l1 = [1, 3, 5]
l2 = [2, 4, 6]


# l = l1 + l2
# l1.insert(3, 0)
# print(l1)


def mergelist(nums1, nums2):
    """两个数组都是有序的时候进行合并"""
    begin = 0
    for n1 in nums1:
        for i in range(begin, len(nums2)):
            if n1 < nums2[i]:
                nums2.insert(i, n1)
                begin = i + 1
                break
            elif i == len(nums2) - 1:
                nums2.insert(len(nums2), n1)
                begin = len(nums2)
                break
    return nums2


if __name__ == '__main__':
    l = mergelist(l1, l2)
    print(l)
