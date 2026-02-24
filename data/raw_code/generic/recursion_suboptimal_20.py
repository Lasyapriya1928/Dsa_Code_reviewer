def find_max(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    rest = find_max(arr, index + 1)
    return arr[index] if arr[index] > rest else rest