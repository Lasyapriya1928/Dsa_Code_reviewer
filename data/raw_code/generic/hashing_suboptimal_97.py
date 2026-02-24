def distinct_count(nums):
    seen = set()
    for n in nums:
        seen.add(n)
    return len(seen)