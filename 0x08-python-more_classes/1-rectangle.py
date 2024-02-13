#!/usr/bin/python3
""" class Rectangle that defines a rectangle based on 0-rectangle.py"""


class Rectangle:
    """Defines a rectangle based on 0-rectangle.py"""
    def __init__(self, width=0, height=0):
        """instantiation of our class object
        Args:
            width (int): the value of the width of rectangle
            height (int): the value of the height of a rectangle
"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Public Getter attribute for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """public getter method for width attribute of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute for the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter method for the height attribute for the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
