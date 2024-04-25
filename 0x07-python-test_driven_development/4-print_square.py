#!/usr/bin/python3
"""
This is a module with a function that prints a square with the character #
"""


def print_square(size):
    """
    This is a function that prints a square with the character #

    Args:
    size: is the size length of the square

    Returns:
    a square of given length dimensions from argumment size

    Raises:
    TypeError: if size is not an integer or float raise TypeError
    ValueError: if the integer or float is less than 0, raise a ValueError
    """
    symbl = "#"
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
        if size >= 0:
            for i in range(size):
                print("{}\n".format((symbl)*i))

    if isinstance(size, float):
        if size < 0:
            raise ValueError("size must be >=0")
        if size >= 0:
            for i in range(size):
                print("{}\n".format((symbl)*i))

