def first_equal_pair(arr):
    for i in range(len(arr)):
        j = i + 1
        while j < len(arr):
            if arr[i] == arr[j]:
                return (i, j)
            j += 1
    return None