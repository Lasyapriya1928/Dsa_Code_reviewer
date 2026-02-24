def first_negative_pair(arr):
    for i, x in enumerate(arr):
        for j, y in enumerate(arr):
            if i < j:
                if x < 0 and y < 0:
                    return (i, j)
    return None