from typing import List


class Solution:
    def getRow(self, rowIndex):
        result = []
        for i in range(rowIndex + 1):
            result.append(self.getC(rowIndex, i))
        return result

    def getC(self, rowIndex, i):
        a = min(rowIndex, i)
        b = rowIndex - a
        c = 1
        for j in range(1, a + 1):
            c *= (b + j)
            c /= j
        return int(c)


if __name__ == '__main__':

    list = []
    for i in range(34):
        list.append(Solution().getRow(i))
    print(list)
