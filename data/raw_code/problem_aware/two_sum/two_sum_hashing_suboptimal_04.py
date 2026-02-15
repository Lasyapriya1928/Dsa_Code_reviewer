def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        for key in seen:
            if nums[i] + key == target:
                return [seen[key], i]
        seen[nums[i]] = i

    return []
"""num_loops = 2
max_loop_depth = 2
uses_dict = 1
"""