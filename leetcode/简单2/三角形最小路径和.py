from typing import List


# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形：
#
# [
#     [2],
#     [3,4],
#     [6,5,7],
#     [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 第一列只能计算上一行的第一列的最小路径，其他的可以计算上一行的 col,col-1这两个列的最小路径

# 解题方案
# 1.求出第几行的第列的最小路径和
# 2.再求出最后一行的所有列的最小路径和，然后取最小值即可
# 这个方式是可以的，但是消耗时间太长，在数据太大的时候，计算消耗的时间太长，要有别的方法才行。
# 进行改进，用一个字典来记录相应坐标位置的最小和  如 {(0,0):2,(1,0):3,(1,1):4},

class Solution:

    def __init__(self):
        self.dict = {}

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        len1 = len(triangle)
        minSum = self.getminMNTotal(triangle, len1 - 1, 0)
        for i in range(1, len1):
            minSum = min(minSum, self.getminMNTotal(triangle, len1 - 1, i))
        return minSum

    def getminMNTotal(self, triange: List[List[int]], m, n) -> int:
        """求m行n列的最小路径和"""
        if (m, n) in self.dict.keys():
            return self.dict[(m, n)]
        if m == 0:
            self.dict[(m, n)] = triange[0][0]
        else:
            if n == 0:
                self.dict[(m, n)] = triange[m][0] + self.getminMNTotal(triange, m - 1, 0)
            elif m == n:
                self.dict[(m, n)] = triange[m][n] + self.getminMNTotal(triange, m - 1, n - 1)
            else:
                self.dict[(m, n)] = triange[m][n] + min(self.getminMNTotal(triange, m - 1, n - 1),
                                                        self.getminMNTotal(triange, m - 1, n))
        return self.dict[(m, n)]


if __name__ == '__main__':
    x = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    y = Solution().minimumTotal(x)
    print(y)
