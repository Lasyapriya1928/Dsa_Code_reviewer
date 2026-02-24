def shift_zeros_right(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
    while left < len(nums):
        nums[left] = 0
        left += 1
    return nums