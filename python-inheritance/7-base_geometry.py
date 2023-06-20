#!/usr/bin/python3
"""
Crating empty class BaseGeometry.
"""


class BaseGeometry:
    """
    BaseGeometry class definition
    """

    def area(self):
        """
        Raise an exception indicating that
        the area() method is not implemented.

        Raises:
            Exception: Indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer.

        Args:
            name (str): The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
