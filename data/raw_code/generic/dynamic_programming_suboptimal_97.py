def count_increasing_subsequences(nums):
    n = len(nums)
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] += dp[j]
    return sum(dp)