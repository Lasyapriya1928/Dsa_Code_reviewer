def frequency_pairs(nums):
    freq = {}
    for val in nums:
        freq.setdefault(val, 0)
        freq[val] += 1
    pairs = 0
    for value in freq.values():
        if value > 1:
            pairs += value - 1
    return pairs