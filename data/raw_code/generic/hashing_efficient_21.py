def two_sum_indices(arr, target):
    lookup = {}
    for index in range(len(arr)):
        needed = target - arr[index]
        if needed in lookup:
            return (lookup[needed], index)
        lookup[arr[index]] = index
    return None