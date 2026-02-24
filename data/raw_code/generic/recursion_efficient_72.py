def min_in_matrix(matrix, r=0, c=0, current=None):
    if r == len(matrix):
        return current
    if c == len(matrix[0]):
        return min_in_matrix(matrix, r + 1, 0, current)
    value = matrix[r][c]
    if current is None or value < current:
        current = value
    return min_in_matrix(matrix, r, c + 1, current)