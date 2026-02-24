def pair_exists(nums, k):
    values = set()
    for num in nums:
        if num - k in values:
            return True
        values.add(num)
    return False