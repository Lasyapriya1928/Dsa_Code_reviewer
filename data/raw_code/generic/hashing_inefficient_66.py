def map_values_to_counts(nums):
    counts = {}
    i = 0
    while i < len(nums):
        val = nums[i]
        if val not in counts:
            counts[val] = 1
        else:
            counts[val] += 1
        i += 1
    return counts