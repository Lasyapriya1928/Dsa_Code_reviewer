def count_subarrays_with_k(nums, k):
    prefix = 0
    freq = {0: 1}
    total = 0
    for value in nums:
        prefix += value
        total += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1
    return total