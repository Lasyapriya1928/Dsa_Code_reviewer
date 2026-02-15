def hashing_two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return True
        seen[num] = i
    return False

#Pattern: hashing
