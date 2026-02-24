def flatten_list(lst):
    if not lst:
        return []
    head = lst[0]
    tail = lst[1:]
    if isinstance(head, list):
        return flatten_list(head) + flatten_list(tail)
    return [head] + flatten_list(tail)