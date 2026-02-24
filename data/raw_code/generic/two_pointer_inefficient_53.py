def reverse_pairs(nums):
    left = 0
    right = len(nums) - 1
    result = []
    while left <= right:
        result.append(nums[left])
        if left != right:
            result.append(nums[right])
        left += 1
        right -= 1
    return result