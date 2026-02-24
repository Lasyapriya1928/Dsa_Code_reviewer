def sum_positive(nums, idx=0):
    if idx == len(nums):
        return 0
    val = nums[idx] if nums[idx] > 0 else 0
    return val + sum_positive(nums, idx + 1)