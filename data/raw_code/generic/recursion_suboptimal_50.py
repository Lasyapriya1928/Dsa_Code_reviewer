def find_index(arr, target, i=0):
    if i >= len(arr):
        return -1
    if arr[i] == target:
        return i
    return find_index(arr, target, i + 1)