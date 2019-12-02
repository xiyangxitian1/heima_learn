class Solution:
    def reverse(self, x: int) -> int:
        maxN = 2 ** 31 - 1
        minN = -2 ** 31
        if x > maxN or x < minN:
            return 0
        if x > 0:
            str1 = str(x)
            l = list(str1)
            l.reverse()
            result = ''
            for i in l:
                result += i
            while result.startswith('0'):
                result = result[1:]
            if int(result) > maxN or int(result) < minN:
                return 0
            return result
        elif x < 0:
            str1 = str(x)
            str0 = str1[0]
            str1 = str1[1:]
            l = list(str1)
            l.reverse()
            result = ''
            for i in l:
                result += i
            while result.startswith('0'):
                result = result[1:]
            result = str0 + result
            if int(result) > maxN or int(result) < minN:
                return 0
            return result
        else:
            return x


if __name__ == '__main__':
    s = Solution()
    # x = 1534236469  # 数据很大的时候结果显示就不正常
    # x = 100
    # [−2**31,  2**31 − 1]   这个返回外的会溢出 返回0
    x = 1534236469  # 这种超大的数要返回0
    result = s.reverse(x)
    print(result)
