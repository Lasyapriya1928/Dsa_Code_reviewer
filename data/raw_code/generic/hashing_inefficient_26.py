def unique_elements(nums):
    seen = {}
    result = []
    for val in nums:
        if val not in seen:
            seen[val] = True
            result.append(val)
    return result