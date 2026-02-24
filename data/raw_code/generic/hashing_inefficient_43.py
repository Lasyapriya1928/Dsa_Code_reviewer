def merge_counts(a, b):
    result = {}
    for key in a:
        result[key] = a[key]
    for key in b:
        if key in result:
            result[key] += b[key]
        else:
            result[key] = b[key]
    return result