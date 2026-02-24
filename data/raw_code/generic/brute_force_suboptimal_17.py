def count_equal_pairs(arr):
    total = 0
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] == arr[j]:
                total += 1
            j += 1
        i += 1
    return total