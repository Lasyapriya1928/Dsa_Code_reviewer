def count_binary_strings(n):
    dp = [[0]*2 for _ in range(n)]
    dp[0][0] = dp[0][1] = 1
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]
    return dp[-1][0] + dp[-1][1]