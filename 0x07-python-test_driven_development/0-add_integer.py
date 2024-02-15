#!/usr/bin/python3
"""Module add_integer
adds two integers
"""


def add_integer(a, b=98):
    """Raises a typeerror if values aren't
    ints or floats
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
