def count_partitions(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return count_partitions(n - 1) + count_partitions(n - 2)