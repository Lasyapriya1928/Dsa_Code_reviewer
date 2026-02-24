def fast_fib(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fast_fib(n - 1, memo) + fast_fib(n - 2, memo)
    return memo[n]