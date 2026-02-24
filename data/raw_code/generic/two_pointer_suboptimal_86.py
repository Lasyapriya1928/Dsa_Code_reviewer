def merge_forward_backward(a, b):
    i = 0
    j = len(b) - 1
    result = []
    while i < len(a) or j >= 0:
        if i < len(a):
            result.append(a[i])
            i += 1
        if j >= 0:
            result.append(b[j])
            j -= 1
    return result