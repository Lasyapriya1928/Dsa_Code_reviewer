def reverse_half(nums):
    left = 0
    right = len(nums) // 2 - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums