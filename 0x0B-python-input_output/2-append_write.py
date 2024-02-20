#!/usr/bin/python3
"""defines a function thaat appends a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """appends a string at the end if the file and returns the number
    returns the number of characters added"""
    with open(filename, 'a', encoding='utf-8') as f:
        num_of_chars = f.write(text)
    return num_of_chars
