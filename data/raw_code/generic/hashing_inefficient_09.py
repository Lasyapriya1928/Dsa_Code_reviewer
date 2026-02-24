def count_pairs(nums):
    seen = {}
    total = 0
    for x in nums:
        if x in seen:
            total += seen[x]
            seen[x] += 1
        else:
            seen[x] = 1
    return total