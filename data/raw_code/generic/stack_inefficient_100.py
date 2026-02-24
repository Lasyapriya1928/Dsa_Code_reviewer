def stack_merge(a, b):
    stack = []
    for x in a:
        stack.append(x)
    for y in b:
        stack.append(y)
    return stack