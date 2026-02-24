def sum_odd(nums, i=0):
    if i == len(nums):
        return 0
    value = nums[i] if nums[i] % 2 else 0
    return value + sum_odd(nums, i + 1)