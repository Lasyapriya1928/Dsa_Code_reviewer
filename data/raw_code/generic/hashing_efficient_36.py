def pair_sum_count(nums, target):
    seen = {}
    total = 0
    for val in nums:
        needed = target - val
        total += seen.get(needed, 0)
        seen[val] = seen.get(val, 0) + 1
    return total