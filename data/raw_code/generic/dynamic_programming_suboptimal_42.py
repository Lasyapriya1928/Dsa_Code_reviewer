def target_sum(nums, target):
    total = sum(nums)
    if (total + target) % 2:
        return 0
    subset = (total + target) // 2
    dp = [0]*(subset+1)
    dp[0] = 1
    for num in nums:
        for s in range(subset, num-1, -1):
            dp[s] += dp[s-num]
    return dp[subset]