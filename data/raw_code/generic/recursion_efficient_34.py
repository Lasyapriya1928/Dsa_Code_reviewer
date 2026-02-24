def search_matrix(matrix, target, row=0):
    if row == len(matrix):
        return False
    if target in matrix[row]:
        return True
    return search_matrix(matrix, target, row + 1)