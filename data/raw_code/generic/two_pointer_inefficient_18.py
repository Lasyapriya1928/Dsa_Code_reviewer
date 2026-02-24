def pair_closest_sum(nums, target):
    nums.sort()
    l = 0
    r = len(nums) - 1
    best = float("inf")
    while l < r:
        total = nums[l] + nums[r]
        best = min(best, abs(total - target))
        if total < target:
            l += 1
        else:
            r -= 1
    return best