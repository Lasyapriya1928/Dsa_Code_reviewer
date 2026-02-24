def climb_stairs_dp(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] += dp[i - 1]
        if i > 1:
            dp[i] += dp[i - 2]
    return dp[n]