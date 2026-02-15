def two_sum(nums, target):
    pairs = []
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            pairs.append((i, j, nums[i] + nums[j]))

    for i, j, s in pairs:
        if s == target:
            return [i, j]

    return []
"""num_loops = 2
max_loop_depth = 2
uses_list = 1
lines_of_code ↑
"""