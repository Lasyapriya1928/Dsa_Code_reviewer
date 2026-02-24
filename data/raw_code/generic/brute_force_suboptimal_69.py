def first_duplicate_value(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if arr[i] == arr[j]:
                    return arr[i]
    return None