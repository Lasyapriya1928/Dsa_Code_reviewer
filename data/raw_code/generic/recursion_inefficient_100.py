def sum_nested(lst):
    if not lst:
        return 0
    head = lst[0]
    tail = lst[1:]
    if isinstance(head, list):
        return sum_nested(head) + sum_nested(tail)
    return head + sum_nested(tail)