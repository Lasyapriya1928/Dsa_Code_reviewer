def max_sum_rectangle(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    for left in range(cols):
        temp = [0]*rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]
            curr = temp[0]
            best = temp[0]
            for num in temp[1:]:
                curr = max(num, curr+num)
                best = max(best, curr)
            max_sum = max(max_sum, best)
    return max_sum