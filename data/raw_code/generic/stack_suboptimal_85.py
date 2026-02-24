def remove_duplicate_chars(s):
    stack = []
    for ch in s:
        if ch not in stack:
            stack.append(ch)
    return "".join(stack)