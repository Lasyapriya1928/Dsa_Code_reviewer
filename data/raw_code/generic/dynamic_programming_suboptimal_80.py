def max_points(points):
    m, n = len(points), len(points[0])
    dp = points[0][:]
    for i in range(1, m):
        left = dp[:]
        right = dp[:]
        for j in range(1, n):
            left[j] = max(left[j], left[j-1]-1)
        for j in range(n-2, -1, -1):
            right[j] = max(right[j], right[j+1]-1)
        for j in range(n):
            dp[j] = points[i][j] + max(left[j], right[j])
    return max(dp)