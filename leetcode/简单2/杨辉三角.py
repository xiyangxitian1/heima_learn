from typing import List

"""
杨辉三角
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
下面一行是由上面一行推导而来
每个数字是由上一行的两个数字。[row][col] = [row-1][col]+[row-1][col-1]  如果[row-1][col]没有就是0
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return None
        if numRows == 1:
            return [[1]]
        else:
            len1 = numRows // 2
            if numRows % 2 != 0:
                len1 += 1
            list1 = self.generate(numRows - 1)
            list11 = list1[-1]  # 上一行的数据
            list2 = [1 if i == 0 else list11[i] + list11[i - 1] for i in range(len1)]
            list1.append(list2 + list(reversed(list2)) if numRows % 2 == 0 else list2 + list(reversed(list2[:-1])))
            return list1


if __name__ == '__main__':
    oSolution = Solution()
    list1 = oSolution.generate(0)
    print(list1)
    list1 = oSolution.generate(5)
    print(list1)
