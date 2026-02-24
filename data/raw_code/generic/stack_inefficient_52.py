def manual_stack_reverse(nums):
    stack = []
    for n in nums:
        stack.append(n)
    reversed_list = []
    while len(stack) > 0:
        reversed_list.append(stack.pop())
    return reversed_list