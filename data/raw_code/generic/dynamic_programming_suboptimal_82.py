def max_sum_divisible_by_three(nums):
    dp = [0, float('-inf'), float('-inf')]
    for num in nums:
        prev = dp[:]
        for r in range(3):
            dp[(r + num) % 3] = max(dp[(r + num) % 3], prev[r] + num)
    return dp[0]