def staircase_k_steps(n, k):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for step in range(1, k+1):
            if i-step >= 0:
                dp[i] += dp[i-step]
    return dp[n]