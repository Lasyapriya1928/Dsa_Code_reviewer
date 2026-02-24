def reverse_string_stack(s):
    stack = []
    for ch in s:
        stack.append(ch)
    result = []
    while stack:
        result.append(stack.pop())
    return "".join(result)