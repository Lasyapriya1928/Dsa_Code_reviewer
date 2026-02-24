def group_by_remainder(nums):
    groups = {}
    for n in nums:
        r = n % 4
        if r not in groups:
            groups[r] = []
        groups[r].append(n)
    return groups