def tail_sum(arr):
    def helper(i, acc):
        if i == len(arr):
            return acc
        return helper(i + 1, acc + arr[i])
    return helper(0, 0)