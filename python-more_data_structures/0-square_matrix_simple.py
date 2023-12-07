def square_matrix_simple(matrix=[]):
    result_matrix = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix