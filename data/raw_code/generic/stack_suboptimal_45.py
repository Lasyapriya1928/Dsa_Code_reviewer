def two_stack_queue(operations):
    s1 = []
    s2 = []
    result = []
    for op in operations:
        if op[0] == "push":
            s1.append(op[1])
        elif op[0] == "pop":
            if not s2:
                while s1:
                    s2.append(s1.pop())
            if s2:
                result.append(s2.pop())
    return result