def first_repeating(nums):
    seen = set()
    for val in nums:
        if val in seen:
            return val
        seen.add(val)
    return None