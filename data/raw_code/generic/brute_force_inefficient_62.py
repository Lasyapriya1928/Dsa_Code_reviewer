def triplet_strict_increasing(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i < j < k:
                    if arr[i] < arr[j] < arr[k]:
                        return True
    return False