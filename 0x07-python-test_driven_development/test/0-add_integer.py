#!/usr/bin/python3
"""A function that adds 2 integers"""


def add_integer(a, b=98):
    """Function that adds two integers.

    Args:
        a: the first integer in the parameter list
        b: the second integer

    Raises:
        TypeError: if either of a and b is an non_integer and non-float
    Returns:
        returns an integer addition of a and b
    Examples:
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
