def max_crossing_sum(nums, left, mid, right):
    left_sum = float('-inf')
    s = 0
    for i in range(mid, left - 1, -1):
        s += nums[i]
        left_sum = max(left_sum, s)

    right_sum = float('-inf')
    s = 0
    for i in range(mid + 1, right + 1):
        s += nums[i]
        right_sum = max(right_sum, s)

    return left_sum + right_sum

def helper(nums, left, right):
    if left == right:
        return nums[left]

    mid = (left + right) // 2
    return max(
        helper(nums, left, mid),
        helper(nums, mid + 1, right),
        max_crossing_sum(nums, left, mid, right)
    )

def max_subarray(nums):
    return helper(nums, 0, len(nums) - 1)
"""has_recursion = 1
num_loops = 2
uses_list = 0
"""