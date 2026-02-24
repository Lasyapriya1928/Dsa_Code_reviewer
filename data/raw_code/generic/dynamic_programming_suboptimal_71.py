def max_score_sightseeing_pair(values):
    n = len(values)
    dp = [0]*n
    best = values[0]
    for j in range(1, n):
        dp[j] = best + values[j] - j
        best = max(best, values[j] + j)
    return max(dp[1:])