def repeating_prefix_sum(nums):
    total = 0
    seen = {0}
    for value in nums:
        total += value
        if total in seen:
            return True
        seen.add(total)
    return False