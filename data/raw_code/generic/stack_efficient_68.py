def next_greater_left(nums):
    stack = []
    result = []
    for n in nums:
        while stack and stack[-1] <= n:
            stack.pop()
        result.append(stack[-1] if stack else -1)
        stack.append(n)
    return result