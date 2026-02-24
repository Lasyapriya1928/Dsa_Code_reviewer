def pair_difference_equals(nums, value):
    for left in range(len(nums)):
        for right in range(len(nums)):
            if left != right:
                if abs(nums[left] - nums[right]) == value:
                    return True
    return False