def two_pointer_remove_duplicates(nums):
    left = 0
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]
    return left + 1

#Pattern: twopointer
