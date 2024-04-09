#!/usr/bin/python3

"""Defines a function for adding two integers"""

def add_integer(a, b=98):
    """Float arguments are typecast to ints before addition is perfomed."""
    """Raises: TypeError: If either a or b is a non-integer and non-float."""

    if((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("A must be an integer")
    if((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("B must be an integer")

    """Function returns a sum of integer a and b"""
    return (int(a) + int(b))
