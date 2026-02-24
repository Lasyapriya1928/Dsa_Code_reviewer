def has_adjacent_equal(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if abs(i - j) == 1 and arr[i] == arr[j]:
                    return True
    return False