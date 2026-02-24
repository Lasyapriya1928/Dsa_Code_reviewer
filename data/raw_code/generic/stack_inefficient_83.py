def stack_accumulate(nums):
    stack = []
    for n in nums:
        stack.append(n)
    acc = 0
    while stack:
        acc += stack.pop()
    return acc