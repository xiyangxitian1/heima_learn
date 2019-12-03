import time


class Solution:

    # 计算这个特别的费时 n =38时需要4.4秒以上
    def fn(self, n):
        if n == 3 or n == 4:
            return 1
        else:
            return self.fn(n - 1) + self.fn(n - 2)

    def getargs(self, n):
        return self.fn(n + 1), self.fn(n)

    # def climbStairs1(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     elif n == 2:
    #         return 2
    #     else:
    #         return self.climbStairs(n - 1) + self.climbStairs(n - 2)

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
    x = 2
    # y = Solution().climbStairs1(x)
    # print('共用时：', time.time() - begin)  # 共用时： 12.044380903244019
    # y = Solution().climbStairs(x)
    # print('共用时：', time.time() - begin)  # 优化后： 共用时： 11.611317157745361
    # print(y)
    # print(Solution().fn(38))
    print(Solution().climbStairs(x))
    print('共用时：', time.time() - begin)
# fn(3) = 1 * fn(2) + 1 * fn(1)
# fn(4) = 2 * fn(2) + 1 * fn(1)
# fn(5) = 3 * fn(2) + 2 * fn(1)
# fn(6) = 5 * fn(2) + 3 * fn(1)
# fn(7) = 8 * fn(2) + 5 * fn(1)
# 发现规律，这正是蜚波那切数列
# 可以和 这种数列来表示了。


# fn(3) = fn(2) + fn(1)

# fn(4) = fn(3) + fn(2)
# fn(4) = fn(2) + fn(1) + fn(2)
# fn(4) = 2 * fn(2) + fn(1)

# fn(5) = fn(4) + fn(3)
# fn(5) = 2 * fn(2) + fn(1) + fn(2) + fn(1)
# fn(5) = 3 * fn(2) + 2 * fn(1)

# fn(6) = fn(5) + fn(4)
# fn(6) = 5 * fn(2) + 3 * fn(1)

# fn(7) = 8 * fn(2) + 5 * fn(1)
