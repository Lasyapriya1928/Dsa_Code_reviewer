def helper(nums, target, i, j):
    if i >= len(nums):
        return []
    if j >= len(nums):
        return helper(nums, target, i + 1, i + 2)
    if nums[i] + nums[j] == target:
        return [i, j]
    return helper(nums, target, i, j + 1)

def two_sum(nums, target):
    return helper(nums, target, 0, 1)
"""has_recursion = 1
num_loops = 0
"""