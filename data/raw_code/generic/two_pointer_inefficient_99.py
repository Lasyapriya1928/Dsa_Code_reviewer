def swap_edges(nums):
    if len(nums) > 1:
        nums[0], nums[-1] = nums[-1], nums[0]
    return nums