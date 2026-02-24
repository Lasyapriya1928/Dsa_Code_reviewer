def reverse_prefix(nums, k):
    left = 0
    right = k
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums