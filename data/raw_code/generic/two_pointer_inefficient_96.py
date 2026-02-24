def reverse_even_indices(nums):
    left = 0
    right = len(nums) - 2
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 2
        right -= 2
    return nums