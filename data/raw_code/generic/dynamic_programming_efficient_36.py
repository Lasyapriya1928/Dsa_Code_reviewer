def minimum_partition_difference(nums):
    total = sum(nums)
    target = total//2
    dp = [False]*(target+1)
    dp[0] = True
    for num in nums:
        for t in range(target, num-1, -1):
            dp[t] |= dp[t-num]
    for t in range(target, -1, -1):
        if dp[t]:
            return total - 2*t