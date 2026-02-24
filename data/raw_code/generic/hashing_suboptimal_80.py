def unique_value_count(nums):
    store = {}
    for n in nums:
        store[n] = True
    return len(store.keys())