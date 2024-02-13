#!/usr/bin/python3
""" Defines a square printing function"""


def print_square(size):
    """ it prints a square with the character #
    Args:
        size (int): the value of size of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        for i in range(size):
            if i != size - 1:
                print('#', end='')
            else:
                print('#')


if __name__ == '__main__':
    print_square()
