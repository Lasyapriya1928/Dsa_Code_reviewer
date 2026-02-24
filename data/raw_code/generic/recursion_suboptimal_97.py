def count_zero(nums, i=0):
    if i >= len(nums):
        return 0
    return (1 if nums[i] == 0 else 0) + count_zero(nums, i + 1)