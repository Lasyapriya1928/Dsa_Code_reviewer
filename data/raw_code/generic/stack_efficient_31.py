def next_greater_circular(nums):
    n = len(nums)
    stack = []
    res = [-1] * n
    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            res[stack.pop()] = nums[i % n]
        if i < n:
            stack.append(i)
    return res