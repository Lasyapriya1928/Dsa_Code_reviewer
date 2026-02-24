def count_distinct(nums):
    store = {}
    for n in nums:
        store[n] = True
    return len(store)