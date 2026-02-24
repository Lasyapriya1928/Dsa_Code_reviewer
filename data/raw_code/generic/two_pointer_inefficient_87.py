def reverse_middle(nums):
    left = len(nums) // 4
    right = len(nums) - len(nums) // 4 - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums