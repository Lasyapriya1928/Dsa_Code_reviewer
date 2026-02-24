def count_subsets(nums, target):
    dp = [[0]*(target+1) for _ in range(len(nums)+1)]
    dp[0][0] = 1
    for i in range(1, len(nums)+1):
        for t in range(target+1):
            dp[i][t] = dp[i-1][t]
            if nums[i-1] <= t:
                dp[i][t] += dp[i-1][t-nums[i-1]]
    return dp[len(nums)][target]