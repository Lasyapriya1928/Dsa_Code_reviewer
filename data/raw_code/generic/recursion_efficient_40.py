def min_value(arr, idx=0):
    if idx == len(arr) - 1:
        return arr[idx]
    rest = min_value(arr, idx + 1)
    return arr[idx] if arr[idx] < rest else rest