def simple_stack_machine(commands):
    stack = []
    for cmd in commands:
        if cmd == "inc" and stack:
            stack[-1] += 1
        elif cmd == "dec" and stack:
            stack[-1] -= 1
        else:
            stack.append(0)
    return stack