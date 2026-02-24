def stack_string_builder(parts):
    stack = []
    for p in parts:
        stack.append(p)
    return "".join(stack)