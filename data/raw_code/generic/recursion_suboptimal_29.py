def product_list(arr, idx=0):
    if idx == len(arr):
        return 1
    return arr[idx] * product_list(arr, idx + 1)