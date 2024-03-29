def change_amount(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] += dp[i-coin]
    return dp[-1]

amount = 5
coins = [1, 2, 5]
print(change_amount(amount, coins))