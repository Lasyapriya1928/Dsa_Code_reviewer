def two_sum_closest(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1
    best = float("inf")
    while left < right:
        total = nums[left] + nums[right]
        if abs(total - target) < abs(best - target):
            best = total
        if total < target:
            left += 1
        else:
            right -= 1
    return best