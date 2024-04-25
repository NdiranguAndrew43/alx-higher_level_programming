#!/usr/bin/python3
"""
This a moduele that will have a function to print 'My name is <first name> <last name>'
"""


def say_my_name(first_name, last_name=""):
    """
    This is a function to print the message 'My name is <first name> <last name>'.

    Args:
    first_name: this is a string passed into the function.
    second_name: this is a string passed into the function.

    Returns:
    The message with the firstname and lastname strings attached
    'My name is <firstname> <lastname>'

    Raises:
    TypeError: raises a TypeError if first_name or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {} {}".format(first_name, last_name))

