def simulate_stack_commands(cmds):
    stack = []
    output = []
    for cmd in cmds:
        if cmd.startswith("add"):
            stack.append(int(cmd.split()[1]))
        elif cmd == "remove" and stack:
            stack.pop()
        elif cmd == "peek" and stack:
            output.append(stack[-1])
    return output