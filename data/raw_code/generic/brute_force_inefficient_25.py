def max_sum_triplet(arr):
    best = float("-inf")
    size = len(arr)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                if i != j and j != k and i != k:
                    s = arr[i] + arr[j] + arr[k]
                    if s > best:
                        best = s
    return best