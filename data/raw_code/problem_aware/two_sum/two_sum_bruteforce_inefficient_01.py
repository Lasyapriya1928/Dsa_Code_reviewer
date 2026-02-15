def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
#Pattern: BruteForce
#Time: O(n²)
#Space: O(1)
"""num_loops = 2
max_loop_depth = 2
uses_dict = 0
"""