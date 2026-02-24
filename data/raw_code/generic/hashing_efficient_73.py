def subarray_count(nums, k):
    running = 0
    store = {0: 1}
    answer = 0
    for num in nums:
        running += num
        if running - k in store:
            answer += store[running - k]
        store[running] = store.get(running, 0) + 1
    return answer