def count_frequency(nums):
    freq = {}
    for x in nums:
        if x in freq:
            freq[x] = freq[x] + 1
        else:
            freq[x] = 1
    total = 0
    for key in freq:
        total += freq[key]
    return total