import time
import math


class Solution:

    # 递归实现太消耗时间与空间了，改成循环的方式
    # def fn(self, n):
    #     if n == 3 or n == 4:
    #         return 1
    #     else:
    #         return self.fn(n - 1) + self.fn(n - 2)
    # 采用循环的方式来实现
    # def fn(self, n):
    #     if n == 3 or n == 4:
    #         return 1
    #     x, y = 1, 1
    #     for i in range(5, n + 1):
    #         myfib = x + y
    #         x = y
    #         y = myfib
    #     return myfib
    # 公式方法来实现
    def fn(self, n):
        n -= 2
        sqrt5 = 5 ** 0.5  # 根号5
        fib = int((math.pow((1 + sqrt5) / 2, n) - math.pow((1 - sqrt5) / 2, n)) / sqrt5)
        return fib

    def getargs(self, n):
        return self.fn(n + 1), self.fn(n)

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a, b = self.getargs(n)
            return 2 * a + b


if __name__ == '__main__':
    begin = time.time()
    x = 38
    x= 3
    print(Solution().climbStairs(x))
    # print(Solution().fn(4))  # 0 1 1 2 3
    print('用时：', time.time() - begin)
