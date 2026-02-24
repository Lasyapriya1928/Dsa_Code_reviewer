def first_pair_with_difference(nums, diff):
    seen = set()
    for value in nums:
        if value - diff in seen or value + diff in seen:
            return True
        seen.add(value)
    return False