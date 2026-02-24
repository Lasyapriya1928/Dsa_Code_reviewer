def element_positions(arr):
    mapping = {}
    i = 0
    while i < len(arr):
        if arr[i] not in mapping:
            mapping[arr[i]] = []
        mapping[arr[i]].append(i)
        i += 1
    return mapping