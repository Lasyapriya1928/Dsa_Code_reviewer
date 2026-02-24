def longest_equal_pair(arr):
    longest = 0
    for i in range(len(arr)):
        length = 0
        for j in range(i, len(arr)):
            if arr[j] == arr[i]:
                length += 1
        if length > longest:
            longest = length
    return longest