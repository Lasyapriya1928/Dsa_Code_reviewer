def remove_target(nums, target):
    left = 0
    for right in range(len(nums)):
        if nums[right] != target:
            nums[left] = nums[right]
            left += 1
    return nums[:left]