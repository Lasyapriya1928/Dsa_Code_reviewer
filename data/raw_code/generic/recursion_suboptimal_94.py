def sum_indices(nums, i=0):
    if i == len(nums):
        return 0
    return i + sum_indices(nums, i + 1)