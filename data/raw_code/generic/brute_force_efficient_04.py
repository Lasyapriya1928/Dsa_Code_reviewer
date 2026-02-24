def has_zero_pair(nums):
    for x in nums:
        for y in nums:
            if x + y == 0:
                return True
    return False