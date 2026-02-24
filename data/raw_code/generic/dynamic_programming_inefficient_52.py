def dice_rolls(n, k, target):
    dp = [[0]*(target+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for t in range(1, target+1):
            for face in range(1, k+1):
                if t-face >= 0:
                    dp[i][t] += dp[i-1][t-face]
    return dp[n][target]