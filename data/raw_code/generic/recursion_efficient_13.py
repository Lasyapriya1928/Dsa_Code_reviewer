def quick_power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / quick_power(x, -n)
    half = quick_power(x, n // 2)
    if n % 2 == 0:
        return half * half
    return x * half * half