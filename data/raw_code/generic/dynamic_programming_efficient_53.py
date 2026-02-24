def largest_sum_of_averages(nums, K):
    n = len(nums)
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    dp = [[0]*(n+1) for _ in range(K+1)]
    for i in range(1, n+1):
        dp[1][i] = prefix[i]/i
    for k in range(2, K+1):
        for i in range(k, n+1):
            for j in range(k-1, i):
                dp[k][i] = max(dp[k][i], dp[k-1][j] + (prefix[i]-prefix[j])/(i-j))
    return dp[K][n]