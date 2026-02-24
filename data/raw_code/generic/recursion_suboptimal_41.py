def count_odd(nums, i=0):
    if i >= len(nums):
        return 0
    return (1 if nums[i] % 2 else 0) + count_odd(nums, i + 1)