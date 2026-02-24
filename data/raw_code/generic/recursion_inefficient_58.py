def multiply_list(nums):
    if not nums:
        return 1
    return nums[0] * multiply_list(nums[1:])