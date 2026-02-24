def check_subarray_zero(nums):
    prefix = 0
    seen = set([0])
    for num in nums:
        prefix += num
        if prefix in seen:
            return True
        seen.add(prefix)
    return False