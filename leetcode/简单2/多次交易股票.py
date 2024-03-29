from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """每次都低点买入  高点抛出"""
        if not prices:
            return 0
        min_price = prices[0]  # 买入价格
        max_profit = 0  # 获得利润
        sum_profit = 0  # 总利润
        for p in prices:
            if p < min_price:
                min_price = p
                sum_profit += max_profit
                max_profit = 0
                continue
            if p - min_price > max_profit:
                max_profit = p - min_price
            elif p - min_price < max_profit:
                sum_profit += max_profit  # 把刚才的最大利润交易了
                max_profit = 0
                min_price = p

        return sum_profit + max_profit


if __name__ == '__main__':
    # x = [7, 1, 5, 3, 6, 4]
    # x = [1, 2, 3, 4, 5]
    # x = [7, 6, 4, 3, 1]
    x = [2, 1, 2, 0, 1]
    y = Solution().maxProfit(x)
    print(y)
