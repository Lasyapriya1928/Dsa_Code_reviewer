def simulate_editor(actions):
    stack = []
    for action in actions:
        if action == "undo" and stack:
            stack.pop()
        else:
            stack.append(action)
    return stack