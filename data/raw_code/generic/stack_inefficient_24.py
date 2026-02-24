def simulate_browser(history):
    stack = []
    current = None
    for action in history:
        if action.startswith("visit"):
            if current:
                stack.append(current)
            current = action.split()[1]
        elif action == "back" and stack:
            current = stack.pop()
    return current