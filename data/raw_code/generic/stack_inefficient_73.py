def sum_stack_elements(nums):
    stack = []
    total = 0
    for n in nums:
        stack.append(n)
    while stack:
        total += stack.pop()
    return total