def subarray_sum_equals_k(nums, k):
    running = 0
    store = {0: 1}
    total = 0
    for val in nums:
        running += val
        if running - k in store:
            total += store[running - k]
        store[running] = store.get(running, 0) + 1
    return total