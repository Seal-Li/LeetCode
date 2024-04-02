# 出售股票的最佳时机
def sellOutStock(nums):
    if len(nums) < 2:
        return None

    min_price = nums[0]
    max_profit = 0

    for price in nums[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(price, min_price)
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
max_profit = sellOutStock(prices)
print("最大利润:", max_profit)