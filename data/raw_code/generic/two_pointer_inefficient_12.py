def squares_sorted(nums):
    left = 0
    right = len(nums) - 1
    result = []
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.insert(0, nums[left] ** 2)
            left += 1
        else:
            result.insert(0, nums[right] ** 2)
            right -= 1
    return result