class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''
        a = self.reversestr(a)
        b = self.reversestr(b)
        a_len = len(a)
        b_len = len(b)
        if b_len > a_len:
            # 交换a与b
            temp = a
            a = b
            b = temp

        m, n, f = 0, 0, 0
        for i in range(len(a)):
            if i > len(b) - 1:
                n = 0
            else:
                n = int(b[i])
            m = int(a[i])
            if i == len(a) - 1:
                if m + n + f > 1:
                    if m + n + f > 2:
                        result += '11'
                    else:
                        result += '01'
                else:
                    f = 0
                    result += str(m + n + f)
                break

            if m + n + f > 1:
                if m + n + f > 2:
                    result += '1'
                else:
                    result += '0'
                f = 1
            else:
                result += str(m + n + f)
                f = 0
        return self.reversestr(result)

    def reversestr(self, a):
        a = list(a)
        a.reverse()
        return ''.join(a)


if __name__ == '__main__':
    x = '1010'
    y = '1011'
    # 10101
    print(Solution().addBinary(x, y))
