def divide_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    return divide_sum(arr[:mid]) + divide_sum(arr[mid:])