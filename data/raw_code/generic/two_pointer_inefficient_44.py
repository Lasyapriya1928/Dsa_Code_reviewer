def swap_alternate(nums):
    left = 0
    right = 1
    while right < len(nums):
        nums[left], nums[right] = nums[right], nums[left]
        left += 2
        right += 2
    return nums