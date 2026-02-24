def count_negative(nums, i=0):
    if i >= len(nums):
        return 0
    current = 1 if nums[i] < 0 else 0
    return current + count_negative(nums, i + 1)