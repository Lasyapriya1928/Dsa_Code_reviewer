def count_vowel_permutation(n):
    dp = [1]*5
    for _ in range(1, n):
        a,e,i,o,u = dp
        dp = [
            e+i+u,
            a+i,
            e+o,
            i,
            i+o
        ]
    return sum(dp)