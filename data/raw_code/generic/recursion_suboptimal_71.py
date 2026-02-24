def sum_absolute(nums, i=0):
    if i >= len(nums):
        return 0
    return abs(nums[i]) + sum_absolute(nums, i + 1)