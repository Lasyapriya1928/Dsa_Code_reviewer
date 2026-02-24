def monotonic_decreasing(nums):
    stack = []
    for n in nums:
        while stack and stack[-1] < n:
            stack.pop()
        stack.append(n)
    return stack