def sum_squares(arr, i=0):
    if i == len(arr):
        return 0
    return arr[i] * arr[i] + sum_squares(arr, i + 1)