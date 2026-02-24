def frequency_count(arr):
    result = []
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        result.append(count)
    return result