def process_commands(commands):
    stack = []
    result = []
    for cmd in commands:
        if cmd == "push":
            stack.append(len(stack))
        elif cmd == "pop" and stack:
            result.append(stack.pop())
    return result