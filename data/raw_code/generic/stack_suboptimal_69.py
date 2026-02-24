def simulate_text_editor(actions):
    stack = []
    for act in actions:
        if act == "undo":
            if stack:
                stack.pop()
        else:
            stack.append(act)
    return "".join(stack)