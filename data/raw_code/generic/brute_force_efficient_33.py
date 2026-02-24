def has_pair_difference(arr, diff):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if abs(arr[i] - arr[j]) == diff:
                    return True
    return False