def triplet_sum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    if arr[i] + arr[j] + arr[k] == target:
                        return True
    return False