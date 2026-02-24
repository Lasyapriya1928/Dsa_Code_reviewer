def remove_duplicates(nums):
    seen = {}
    result = []
    for n in nums:
        if n not in seen:
            seen[n] = True
            result.append(n)
    return result