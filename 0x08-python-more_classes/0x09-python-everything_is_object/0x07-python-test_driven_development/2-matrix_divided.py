#!/usr/bin/python3
""" A function taht divides all the elements of a matrix"""


def matrix_divided(matrix, div):
    """ A function that divides all elements of a matrix
    Args:
        matrix (list): a list of lists of integers or floats
        div (int): a number(integer or float)
    Raises:
        TypeError: if arguments in list not int or float and div not int or fl
        ZeroDivisionError: when div is 0
    Returns:
        list: a new matrix
"""
    #check if matrix is a list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    #check if matrix only contains integers/floats
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    #check if div is non-zero
    if not isinstance(div, (int, float)):
        raise ValueError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    #check if each row in the matrix is the same size
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    div_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return div_matrix
