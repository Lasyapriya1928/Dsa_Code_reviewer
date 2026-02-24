def count_occurrences(nums, target):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    if target in counts:
        return counts[target]
    return 0