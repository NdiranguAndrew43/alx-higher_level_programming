#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        cpyM = matrix.copy()

        for i in range (len(matrix)):
            cpyM[i] = list(map(lambda x: x**2, matrix[i]))

        return(cpyM)
