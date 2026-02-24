def count_elements_more_than_once(nums):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    count = 0
    for key in freq:
        if freq[key] > 1:
            count += 1
    return count