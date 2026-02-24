def partition_by_value(nums, value):
    left = 0
    for right in range(len(nums)):
        if nums[right] < value:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums