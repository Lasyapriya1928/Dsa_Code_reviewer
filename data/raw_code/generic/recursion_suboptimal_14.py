def count_occurrences(arr, target, index=0):
    if index == len(arr):
        return 0
    count = 1 if arr[index] == target else 0
    return count + count_occurrences(arr, target, index + 1)