def stack_monotonic(nums):
    stack = []
    result = []

    for num in nums:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
        result.append(stack[-1])

    return result
