def longest_arithmetic_subseq(nums):
    n = len(nums)
    dp = [{} for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[j].get(diff, 1) + 1
            ans = max(ans, dp[i][diff])
    return ans