def delete_and_earn(nums):
    from collections import Counter
    count = Counter(nums)
    values = sorted(count)
    take = skip = 0
    prev = None
    for v in values:
        if prev == v - 1:
            take, skip = skip + v*count[v], max(take, skip)
        else:
            take, skip = max(take, skip) + v*count[v], max(take, skip)
        prev = v
    return max(take, skip)