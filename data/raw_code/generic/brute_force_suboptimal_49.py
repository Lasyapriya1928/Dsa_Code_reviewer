def count_equal_indices(arr):
    count = 0
    for i in range(len(arr)):
        j = 0
        while j < len(arr):
            if i != j and arr[i] == arr[j]:
                count += 1
            j += 1
    return count