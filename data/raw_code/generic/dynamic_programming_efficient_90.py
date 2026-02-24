def count_partitions_diff(nums, diff):
    total = sum(nums)
    if (total + diff) % 2:
        return 0
    target = (total + diff)//2
    dp = [0]*(target+1)
    dp[0] = 1
    for num in nums:
        for t in range(target, num-1, -1):
            dp[t] += dp[t-num]
    return dp[target]