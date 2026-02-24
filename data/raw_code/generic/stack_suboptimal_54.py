def adjacent_pair_removal(nums):
    stack = []
    for n in nums:
        if stack and stack[-1] == n:
            stack.pop()
        else:
            stack.append(n)
    return stack