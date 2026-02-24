def count_inversions_recursive(arr):
    if len(arr) <= 1:
        return 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return count_inversions_recursive(left) + count_inversions_recursive(right)