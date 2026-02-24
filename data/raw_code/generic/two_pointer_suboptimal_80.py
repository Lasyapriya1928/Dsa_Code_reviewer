def merge_reverse(a, b):
    i = len(a) - 1
    j = len(b) - 1
    result = []
    while i >= 0 or j >= 0:
        if i >= 0:
            result.append(a[i])
            i -= 1
        if j >= 0:
            result.append(b[j])
            j -= 1
    return result