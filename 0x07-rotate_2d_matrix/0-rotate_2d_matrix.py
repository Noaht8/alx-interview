#!/usr/bin/python3
"""Rotate 2D Matrix module
"""


def rotate_2d_matrix(matrix):
    """rotate the matrix and update the matrix variable
    """
    new = matrix.copy()
    matrix.clear()
    for i in range(len(new), 0, -1):
        s = list(map(lambda x: x[len(x) - i], reversed(new)))
        matrix.append(s)
