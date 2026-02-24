def count_pairs_sorted(nums, target):
    nums.sort()
    l = 0
    r = len(nums) - 1
    count = 0
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            count += 1
            l += 1
            r -= 1
        elif s < target:
            l += 1
        else:
            r -= 1
    return count