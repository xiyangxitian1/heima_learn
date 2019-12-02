class Solution:
    def myAtoi(self, str: str) -> int:
        maxN = 2 ** 31 - 1
        minN = -2 ** 31
        a = str.replace(' ', '')
        if len(a) == 0 or len(a) == 1 and a in ('+', '-'):
            return 0
        b = a[0]
        if not b.isdigit() and b not in ('+', '-'):
            return 0
        if a.isdigit():
            if int(a) > maxN:
                return maxN
            elif int(a) < minN:
                return minN
            return int(a)
        head = None
        if a.startswith('+') or a.startswith('-'):
            head = a[0]
            a = a[1:]
        if not a[0].isdigit() or a[0] == '0':
            return 0
        # 下面a就是以数字开头了
        result = ''
        while a and a[0].isdigit():
            result += a[0]
            if len(a) > 1:
                a = a[1:]
            else:
                break

        if head:
            if head == '-':
                result = head + result
                result = int(result)
                if result < minN:
                    return minN
        result = int(result)
        if result > maxN:
            return maxN
        return result
        # 不是负号开头所以不可能小于minN 不需要判断了。


if __name__ == '__main__':
    so = Solution()
    x = "91283472332"
    x = "42"
    x = "   -42"
    x = "   +0 123"
    result = so.myAtoi(x)
    print(result)
