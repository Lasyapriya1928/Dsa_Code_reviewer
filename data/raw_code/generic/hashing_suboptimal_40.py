def count_unique_pairs(nums):
    pairs = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            pairs.add((nums[i], nums[j]))
    return len(pairs)