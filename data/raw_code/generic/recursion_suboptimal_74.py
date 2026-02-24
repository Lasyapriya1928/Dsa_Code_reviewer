def find_last_index(arr, target, i=None):
    if i is None:
        i = len(arr) - 1
    if i < 0:
        return -1
    if arr[i] == target:
        return i
    return find_last_index(arr, target, i - 1)