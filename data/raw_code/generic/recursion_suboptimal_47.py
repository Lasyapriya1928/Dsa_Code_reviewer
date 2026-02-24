def contains_value(arr, target, i=0):
    if i == len(arr):
        return False
    if arr[i] == target:
        return True
    return contains_value(arr, target, i + 1)