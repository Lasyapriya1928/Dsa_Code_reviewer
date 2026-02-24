def merge_lists(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge_lists(a[1:], b)
    return [b[0]] + merge_lists(a, b[1:])