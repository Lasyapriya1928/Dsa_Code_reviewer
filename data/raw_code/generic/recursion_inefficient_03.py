def sum_list(arr, index=0):
    if index == len(arr):
        return 0
    return arr[index] + sum_list(arr, index + 1)