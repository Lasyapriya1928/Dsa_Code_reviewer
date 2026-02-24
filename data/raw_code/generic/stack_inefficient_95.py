def stack_insert_bottom(nums, value):
    stack = list(nums)
    temp = []
    while stack:
        temp.append(stack.pop())
    stack.append(value)
    while temp:
        stack.append(temp.pop())
    return stack