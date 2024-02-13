#!/usr/bin/python3
""" Writing a class Rectangle that defines a rectangle"""


class Rectangle:
    """it defines a rectangle based on the 1-rectangle.py
"""
    def __init__(self, width=0, height=0):
        """Insatntiate of our class object
        Args:
            width (int): the value of the width of rectangle
            size (int): the value of the height of rectangle
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
        """Getter method for width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method fot width of rectangle
        Args:
            value (int): the value to input as width
"""
        self.__width = value

    @property
    def height(self):
        """Getter for the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle
        Args:
        value (int): the value to set as height of rectangle
"""
        self.__height = value

    def area(self):
        """calculates the area of a rectangle
        Returns:
            int: the area of rectangle
"""
        a = self.height * self.width
        return a

    def perimeter(self):
        """Returns the rectangular perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            prm = (self.height * 2) + (self.width * 2)
            return prm

    @property
    def height(self):
        """Getter for the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle
        Args:
        value (int): the value to set as height of rectangle
"""
        self.__height = value

    def area(self):
        """calculates the area of a rectangle
        Returns:
            int: the area of rectangle
"""
        a = self.height * self.width
        return a

    def perimeter(self):
        """Returns the rectangular perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            prm = (self.height * 2) + (self.width * 2)
            return (prm)

    def __str__(self):
        """it returns the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for i in range(self.__height):
            [rec.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))
