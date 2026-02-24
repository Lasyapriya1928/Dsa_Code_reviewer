def remove_duplicates_unsorted(nums):
    left = 0
    seen = set()
    for right in range(len(nums)):
        if nums[right] not in seen:
            seen.add(nums[right])
            nums[left] = nums[right]
            left += 1
    return nums[:left]