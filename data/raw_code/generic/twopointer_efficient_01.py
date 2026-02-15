def two_pointer_sorted(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1
    return False

#Pattern: twopointer
