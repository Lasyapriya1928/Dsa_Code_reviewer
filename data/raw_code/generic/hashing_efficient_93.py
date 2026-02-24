def repeated_prefix_sum(nums):
    total = 0
    seen = set()
    for n in nums:
        total += n
        if total in seen:
            return True
        seen.add(total)
    return False