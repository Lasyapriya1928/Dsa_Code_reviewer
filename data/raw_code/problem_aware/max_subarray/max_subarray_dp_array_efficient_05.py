def max_subarray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    max_sum = dp[0]

    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
        max_sum = max(max_sum, dp[i])

    return max_sum
"""num_loops = 1
uses_list = 1
"""