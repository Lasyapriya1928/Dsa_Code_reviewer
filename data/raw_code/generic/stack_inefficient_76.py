def remove_consecutive(nums):
    stack = []
    for n in nums:
        if not stack or stack[-1] != n:
            stack.append(n)
    return stack