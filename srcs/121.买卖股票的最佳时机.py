#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price - min_price > max_profit:
                max_profit = price - min_price
            if price < min_price:
                min_price = price
        return max_profit
# @lc code=end

