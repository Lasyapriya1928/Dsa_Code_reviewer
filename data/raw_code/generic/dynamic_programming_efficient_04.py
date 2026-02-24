def house_robber(nums):
    if not nums:
        return 0
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        take = nums[i] + (dp[i - 2] if i > 1 else 0)
        skip = dp[i - 1]
        dp[i] = max(take, skip)
    return dp[-1]