def pairwise_cancel(nums):
    stack = []
    for n in nums:
        if stack and stack[-1] + n == 0:
            stack.pop()
        else:
            stack.append(n)
    return stack