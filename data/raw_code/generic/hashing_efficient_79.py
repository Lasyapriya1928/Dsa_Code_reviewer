def detect_cycle_prefix(nums):
    prefix = 0
    seen = {}
    for i in range(len(nums)):
        prefix += nums[i]
        if prefix in seen:
            return (seen[prefix], i)
        seen[prefix] = i
    return None