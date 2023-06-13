#!/usr/bin/python3
"""Creating the square class whit Private instance attribute: size"""


class Square:
    """Square class definition and Instantiation with size optional size"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """Public instance method that returns the current square area"""

    def area(self):
        return self.__size * self.__size
