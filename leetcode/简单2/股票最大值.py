from typing import List
import 一个越长列表


# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# 注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        minP = min(prices)
        maxP = max(prices)
        try:
            prices.index(maxP, prices.index(minP))
        except ValueError:
            pass
        else:
            return maxP - minP
        minP = prices[0]
        maxPro = 0
        for p in prices[1:]:
            if minP > p:
                minP = p
            if p - minP > maxPro:
                maxPro = p - minP
        return maxPro

    def maxProfit(self, prices: List[int]) -> int:
        """
        第二种解决，把构造一个数组，再求最大子序和
            这种速度比上一种更快
        :param prices:
        :return:
        """
        if not prices or len(prices) == 1:
            return 0
        minP = min(prices)
        maxP = max(prices)
        try:
            prices.index(maxP, prices.index(minP))
        except ValueError:
            pass
        else:
            return maxP - minP
        # 构造数组，就是每两天的利润差
        pArray = []
        for i in range(len(prices) - 1):
            pArray.append(prices[i + 1] - prices[i])
        return self.maxSubArray(pArray)

    def maxSubArray(self, nums):
        """
        最大子数组和
        :param nums:
        :return:
        """
        anx = nums[0]
        sum = 0
        for n in nums:
            if sum > 0:
                sum += n
            else:
                sum = n
            anx = max(sum, anx)  # 永远只记录最大值
        return max(anx, 0)  # 因为要求最小返回0，所以这样


if __name__ == '__main__':
    # x = [1, 2, 3, 4, 5]
    # x = [7, 1, 5, 3, 6, 4]
    # x = [7, 6, 4, 3, 1]
    x = 一个越长列表.max_len_list
    a = Solution().maxProfit(x)
    print(a)
