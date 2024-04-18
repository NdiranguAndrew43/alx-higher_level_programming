#!/usr/bin/python3
"""
This is a module with a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    This is a function thay divides all the elemnts of a matrix


    Args:
    matrix: this is a matrix of lists containing elements
    div: the integer that each element will be divided by

    Returns:
    A matrix of the results from the division

    Raises:
    TypeError is raised when the matrix is not a list of integers and floats
    TypeError is raised when the rows in the matrix are not the same size
    TypeError is raised when div is not an integer or float
    ZeroDivisionError is raised when div is equal to zero
    """
    errmsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errmsg)
    if not isinstance(matrix, list):
        raise TypeError(errmsg)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(errmsg)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(errmsg)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(errmsg)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lists] for lists in matrix]
