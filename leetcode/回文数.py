class Solution:
    """判断是否是回文数，(试着不要用转字符串的方式）
        1.可以把数分一半，然后和另一半比较来进行判断
        2.还可以设两个指针从两头向中间移动进行对比
    """

    #  x 是整数
    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            l = []
            while x // 10 != 0:
                l.append(x % 10)
                x = x // 10
            l.append(x)
            # print(l)
            left, right = 0, len(l) - 1
            while left < right:
                if l[left] == l[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

    #  x 是整数
    def isPalindrome(self, x: int) -> bool:
        """用字符串的方式来"""
        str1 = str(x)
        if str1.startswith('-1'):
            return False
        else:
            len1 = len(str1)
            if len1 > 1:
                half_len = len1 // 2
                leftStr = str1[:half_len]
                rightStr = str1[half_len:]
                if len1 % 2 != 0:
                    rightStr = rightStr[1:]
                if leftStr[::-1] != rightStr:
                    return False
            return True


if __name__ == '__main__':
    solution = Solution()
    x = 134431
    result = solution.isPalindrome(x)
    print(result)
