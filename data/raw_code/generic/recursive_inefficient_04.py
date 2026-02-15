def recursion_sum(nums):
    if not nums:
        return 0
    return nums[0] + recursion_sum(nums[1:])

#Pattern: recursive
