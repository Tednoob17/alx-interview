#!/usr/bin/python3
""" Rotate 2d Matrix """


def rotate_2d_matrix(matrix):
    """ Rotate a n * x matrix it 90 degrees clockwise """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    for i in range(n):
        matrix[i].reverse()
