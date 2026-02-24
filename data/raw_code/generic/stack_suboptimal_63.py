def simulate_call_stack(calls):
    stack = []
    completed = []
    for call in calls:
        if call.startswith("start"):
            stack.append(call.split()[1])
        elif call == "end" and stack:
            completed.append(stack.pop())
    return completed