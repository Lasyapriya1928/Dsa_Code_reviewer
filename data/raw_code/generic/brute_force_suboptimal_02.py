def count_duplicates(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                total += 1
    return total