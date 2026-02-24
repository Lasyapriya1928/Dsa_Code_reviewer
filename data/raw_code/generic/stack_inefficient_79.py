def stack_sum_pairs(nums):
    stack = []
    for n in nums:
        if stack:
            stack.append(stack.pop() + n)
        else:
            stack.append(n)
    return stack