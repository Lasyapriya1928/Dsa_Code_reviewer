def has_subarray_multiple(nums, k):
    prefix = 0
    seen = {0: -1}
    for i in range(len(nums)):
        prefix += nums[i]
        mod = prefix % k
        if mod in seen:
            if i - seen[mod] > 1:
                return True
        else:
            seen[mod] = i
    return False