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

#     [2],
#     [5,6],
#     [11,10,13],
#     [16,11,18,16]

#     [11],
#     [9,10],
#     [7,6,10],
#     [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 第一列只能计算上一行的第一列的最小路径，其他的可以计算上一行的 col,col-1这两个列的最小路径

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        while len(triangle) > 1:
            for i in range(len(triangle[-2])):
                if triangle[-2][i] + triangle[-1][i] < triangle[-2][i] + triangle[-1][i + 1]:
                    triangle[-2][i] += triangle[-1][i]
                else:
                    triangle[-2][i] += triangle[-1][i + 1]
            triangle = triangle[:-1]

        return triangle[0][0]


if __name__ == '__main__':
    x = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    y = Solution().minimumTotal(x)
    print(y)
