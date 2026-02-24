def subarray_sum(nums, target):
    prefix = 0
    seen = {0: 1}
    count = 0
    for n in nums:
        prefix += n
        if prefix - target in seen:
            count += seen[prefix - target]
        seen[prefix] = seen.get(prefix, 0) + 1
    return count