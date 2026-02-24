def subarray_sum_count(nums, target):
    running = 0
    freq = {0: 1}
    count = 0
    for value in nums:
        running += value
        count += freq.get(running - target, 0)
        freq[running] = freq.get(running, 0) + 1
    return count