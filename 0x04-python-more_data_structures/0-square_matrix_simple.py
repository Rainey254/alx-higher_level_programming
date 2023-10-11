#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for h in range(len(matrix)):
        new_matrix[h] = list(map(lambda k: k**2, matrix[h]))

    return (new_matrix)
