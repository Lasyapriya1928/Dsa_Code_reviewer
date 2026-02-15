def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []
#Pattern: Hashing
#Time: O(n)
#Space: O(n)
"""num_loops = 1
max_loop_depth = 1
uses_dict = 1
"""