def subarray_with_sum(nums, target):
    prefix = 0
    seen = {0: -1}
    for i, val in enumerate(nums):
        prefix += val
        if prefix - target in seen:
            return (seen[prefix - target] + 1, i)
        if prefix not in seen:
            seen[prefix] = i
    return None