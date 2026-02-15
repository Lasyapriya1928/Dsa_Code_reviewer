def brute_force_matrix_search(matrix, target):
    for row in matrix:
        for val in row:
            if val == target:
                return True
    return False

#Pattern: bruteforce
