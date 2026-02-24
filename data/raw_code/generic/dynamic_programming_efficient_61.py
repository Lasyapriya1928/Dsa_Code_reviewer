def count_derangements(n):
    if n <= 1:
        return 0
    dp = [0]*(n+1)
    dp[1], dp[2] = 0, 1
    for i in range(3, n+1):
        dp[i] = (i-1)*(dp[i-1] + dp[i-2])
    return dp[n]