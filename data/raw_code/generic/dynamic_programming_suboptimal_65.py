def count_orders(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = dp[i-1] * i * (2*i - 1)
    return dp[n]