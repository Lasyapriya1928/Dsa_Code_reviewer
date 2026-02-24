def duplicate_positions(arr):
    pos = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i < j and arr[i] == arr[j]:
                pos.append((i, j))
    return pos