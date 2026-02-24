def monotonic_increasing(nums):
    stack = []
    for value in nums:
        while stack and stack[-1] > value:
            stack.pop()
        stack.append(value)
    return stack