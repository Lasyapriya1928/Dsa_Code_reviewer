def max_alternating_sum(nums):
    n = len(nums)
    dp = [[0]*2 for _ in range(n)]
    dp[0][0] = nums[0]
    dp[0][1] = 0
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + nums[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - nums[i])
    return dp[-1][0]