#!/usr/bin/python3
'''
   Adds two integers
   a (int | float)
   b (int | float)
'''


def add_integer(a, b=0):
    """ Returns the sum of two integers """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
