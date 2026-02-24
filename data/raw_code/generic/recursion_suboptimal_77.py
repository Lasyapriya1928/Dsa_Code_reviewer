def sum_until_zero(nums, i=0):
    if i >= len(nums) or nums[i] == 0:
        return 0
    return nums[i] + sum_until_zero(nums, i + 1)