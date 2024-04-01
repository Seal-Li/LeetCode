# 硬币找零，例如总额为10，零钱面值有[1,2,5]，那么可以组成10元的组合中，零钱张数最少的是[5,5]，两张
def coinChanges(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] += dp[i - coin]
    return dp[-1]

def min_coin_changes(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i-coin]+1, dp[i])
    return dp[amount] if dp[amount] != float('inf') else -1


amount = 11
nums = [1, 2, 5]
print(coinChanges(amount, nums))
print(min_coin_changes(amount, nums))