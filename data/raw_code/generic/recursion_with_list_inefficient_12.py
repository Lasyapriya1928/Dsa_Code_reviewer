def build(n, res):
    if n == 0:
        return res
    res.append(n)
    return build(n - 1, res)
n=10
build(n, [])
