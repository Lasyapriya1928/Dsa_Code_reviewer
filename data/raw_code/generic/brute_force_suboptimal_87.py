def collect_matching_pairs(arr, value):
    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i < j:
                if arr[i] + arr[j] == value:
                    result.append((i, j))
    return result