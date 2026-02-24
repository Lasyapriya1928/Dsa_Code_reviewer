def zero_sum_exists(nums):
    prefix = 0
    memory = set()
    for n in nums:
        prefix += n
        if prefix == 0 or prefix in memory:
            return True
        memory.add(prefix)
    return False