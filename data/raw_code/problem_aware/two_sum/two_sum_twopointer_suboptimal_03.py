def two_sum(nums, target):
    nums_with_index = list(enumerate(nums))
    nums_with_index.sort(key=lambda x: x[1])

    left, right = 0, len(nums_with_index) - 1

    while left < right:
        s = nums_with_index[left][1] + nums_with_index[right][1]
        if s == target:
            return [nums_with_index[left][0], nums_with_index[right][0]]
        elif s < target:
            left += 1
        else:
            right -= 1

    return []
"""num_loops = 1
max_loop_depth = 1
uses_list = 1
uses_dict = 0"""
