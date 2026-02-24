def check_sorted(arr, idx=0):
    if idx == len(arr) - 1:
        return True
    if arr[idx] > arr[idx + 1]:
        return False
    return check_sorted(arr, idx + 1)