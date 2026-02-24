def subarray_sum_zero(nums):
    prefix = 0
    visited = {0}
    for n in nums:
        prefix += n
        if prefix in visited:
            return True
        visited.add(prefix)
    return False