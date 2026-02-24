def count_greater_pairs(arr):
    total = 0
    for left in range(len(arr)):
        for right in range(left + 1, len(arr)):
            if arr[right] > arr[left]:
                total += 1
    return total