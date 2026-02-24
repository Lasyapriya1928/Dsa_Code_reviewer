def longest_equal_zero_one(nums):
    prefix = 0
    seen = {0: -1}
    best = 0
    for i in range(len(nums)):
        prefix += -1 if nums[i] == 0 else 1
        if prefix in seen:
            length = i - seen[prefix]
            if length > best:
                best = length
        else:
            seen[prefix] = i
    return best