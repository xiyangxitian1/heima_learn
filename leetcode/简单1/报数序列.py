"""
特别有意思的报数序列
1      一
11     一个一
21      二个一
1211   一个二一个一
111221  一个一一个二二个一

"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        last_str = self.countAndSay(n - 1)
        len1 = len(last_str)
        #  采取递推的方式
        now_str = last_str[0]
        result = ''
        count = 1
        i = 1
        while i < len1:
            if last_str[i] == now_str:
                count += 1
            else:
                result += str(count) + now_str
                now_str = last_str[i]
                count = 1
            i += 1

        return result + str(count) + now_str


if __name__ == '__main__':
    x = 5
    print(Solution().countAndSay(x))
