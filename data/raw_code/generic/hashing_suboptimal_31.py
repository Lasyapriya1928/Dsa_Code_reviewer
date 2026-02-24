def difference_exists(nums, diff):
    seen = set()
    for number in nums:
        if number - diff in seen or number + diff in seen:
            return True
        seen.add(number)
    return False