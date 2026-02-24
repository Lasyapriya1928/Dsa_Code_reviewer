def max_difference(nums):
    max_diff = float('-inf')
    for i in range(len(nums)):
        for j in range(len(nums)):
            diff = nums[j] - nums[i]
            if diff > max_diff:
                max_diff = diff
    return max_diff