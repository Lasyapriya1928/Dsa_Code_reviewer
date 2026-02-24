def egg_drop(eggs, floors):
    dp = [[0]*(floors+1) for _ in range(eggs+1)]
    for i in range(1, eggs+1):
        dp[i][1] = 1
    for j in range(1, floors+1):
        dp[1][j] = j
    for i in range(2, eggs+1):
        for j in range(2, floors+1):
            dp[i][j] = float('inf')
            for x in range(1, j+1):
                dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][x-1], dp[i][j-x]))
    return dp[eggs][floors]