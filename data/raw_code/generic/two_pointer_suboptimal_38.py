def pair_with_min_difference(nums):
    nums.sort()
    left = 0
    right = 1
    best = float("inf")
    while right < len(nums):
        best = min(best, abs(nums[right] - nums[left]))
        left += 1
        right += 1
    return best