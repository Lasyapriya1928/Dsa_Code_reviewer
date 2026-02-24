def max_profit(prices):
    if not prices:
        return 0
    dp = [0] * len(prices)
    min_price = prices[0]
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        dp[i] = max(dp[i - 1], prices[i] - min_price)
    return dp[-1]