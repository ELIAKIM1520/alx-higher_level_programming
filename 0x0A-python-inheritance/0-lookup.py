#!/usr/bin/python3
"""This Module contains lookup function definition
    to look a list of methods and fields of an object
    """


def lookup(obj):
    """Function that returns the list of available
    attributes and methods of an object
    Arguments:
        obj {[object]} -- object to check
    Returns:
        [list] -- available attributes and methods
    """
    return dir(obj)
