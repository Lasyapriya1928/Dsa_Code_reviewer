def remove_adjacent_pairs(nums):
    stack = []
    for n in nums:
        if stack and stack[-1] == n:
            stack.pop()
        else:
            stack.append(n)
    return stack