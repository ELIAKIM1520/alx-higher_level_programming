#!/usr/bin/python3
""" Writing a class that defines a rectangle based on 3-rectangle.py"""


class Rectangle:
    """Defines a rectangle based on 3-rectangle.py"""
    def __init__(self, width=0, height=0):
        """instantiation of the object
        Args:
        width (int): the value of width of rectangle
        height (int): the value of the height of rectangle
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
        """Getter method for the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width of the rectangle
        Args:
            value (int): the value for width of the rectangle
"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter fot the height of the rectangle
        Args:
            value (int): the value to input as height
"""
        if not isinstance(self, value):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle
        Returns:
            int: the area of a rectangle
"""
        Area = self.width * self.height
        return Area

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            perim = (self.height * 2) + (self.width * 2)
            return perim

    def __str__(self):
        """printss the  rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ''
        rectangle = ''
        for i in range(self.height):
            if i != self.height - 1:
                rectangle += "#" * self.width + '\n'
            else:
                rectangle += "#" * self.width
        return rectangle

    def __repr__(self):
        """returns a string represenattion of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"
