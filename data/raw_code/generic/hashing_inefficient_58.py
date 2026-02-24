def count_by_parity(nums):
    groups = {}
    for n in nums:
        key = n % 2
        if key not in groups:
            groups[key] = 0
        groups[key] += 1
    return groups