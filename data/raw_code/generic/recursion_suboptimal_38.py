def sum_even(arr, i=0):
    if i == len(arr):
        return 0
    add = arr[i] if arr[i] % 2 == 0 else 0
    return add + sum_even(arr, i + 1)