#!/usr/bin/python3

"""
    This is a module that will calculate the sum of two values
"""


def add_integer(a, b=98):
    """
    This is a function that takes two integers and returns their sum.

    Args:
     a: int
     b: int

    Returns:
        the sum of a and b.

    Raises:
        TypeError: if either of the arguments are not an integer.
    """
    
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, str):
        raise TypeError("a must be an integer")
    if isinstance(b, str):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

