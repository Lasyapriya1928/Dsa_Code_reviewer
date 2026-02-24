def max_profit_two_transactions(prices):
    n = len(prices)
    dp = [[0]*3 for _ in range(n)]
    for k in range(1, 3):
        max_diff = -prices[0]
        for i in range(1, n):
            dp[i][k] = max(dp[i-1][k], prices[i] + max_diff)
            max_diff = max(max_diff, dp[i-1][k-1] - prices[i])
    return dp[-1][2]