def first_non_repeating(nums):
    count = {}
    for val in nums:
        count[val] = count.get(val, 0) + 1
    for val in nums:
        if count[val] == 1:
            return val
    return None