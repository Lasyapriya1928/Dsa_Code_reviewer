def count_pairs_with_sum(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1
    count = 0
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            count += 1
            left += 1
            right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1
    return count