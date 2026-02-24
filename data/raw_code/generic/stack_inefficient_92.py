def stack_rotate(nums):
    stack = list(nums)
    if stack:
        first = stack.pop(0)
        stack.append(first)
    return stack