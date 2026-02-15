def helper(n):
    if n == 0:
        return 0
    return helper(n - 1)

def run(n):
    return helper(n)
