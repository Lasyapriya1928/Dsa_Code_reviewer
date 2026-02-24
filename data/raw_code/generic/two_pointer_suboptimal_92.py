def count_pairs_less_than(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1
    count = 0
    while left < right:
        if nums[left] + nums[right] < target:
            count += right - left
            left += 1
        else:
            right -= 1
    return count