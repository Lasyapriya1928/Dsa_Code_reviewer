def count_lesser_pairs(arr):
    count = 0
    for left in range(len(arr)):
        for right in range(len(arr)):
            if left < right and arr[left] > arr[right]:
                count += 1
    return count