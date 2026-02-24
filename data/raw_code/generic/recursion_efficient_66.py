def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    if k < len(left):
        return quick_select(left, k)
    if k == len(left):
        return pivot
    return quick_select(right, k - len(left) - 1)