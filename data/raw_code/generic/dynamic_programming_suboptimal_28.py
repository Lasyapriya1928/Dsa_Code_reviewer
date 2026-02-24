def min_coins(coins, amount):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for a in range(1, amount+1):
        for c in coins:
            if a >= c:
                dp[a] = min(dp[a], dp[a-c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1