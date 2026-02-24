def knight_probability(n, k, row, column):
    dp = [[0]*n for _ in range(n)]
    dp[row][column] = 1
    moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    for _ in range(k):
        new = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for dx, dy in moves:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < n and 0 <= nj < n:
                        new[ni][nj] += dp[i][j] / 8
        dp = new
    return sum(map(sum, dp))