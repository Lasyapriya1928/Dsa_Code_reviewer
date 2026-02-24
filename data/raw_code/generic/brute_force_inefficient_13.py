def smallest_sum_pair(arr):
    best = float('inf')
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                s = arr[i] + arr[j]
                if s < best:
                    best = s
    return best