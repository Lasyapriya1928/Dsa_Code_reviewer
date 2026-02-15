def max_subarray(nums):
    n = len(nums)
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    max_sum = float('-inf')
    for i in range(n):
        for j in range(i + 1, n + 1):
            max_sum = max(max_sum, prefix[j] - prefix[i])

    return max_sum

"""num_loops = 3
max_loop_depth = 2
uses_list = 1
"""