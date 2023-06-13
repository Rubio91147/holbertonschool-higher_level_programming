#!/usr/bin/python3
"""Creating the square class whit Private instance attribute: size"""


class Square():
    '''Initialization of instance attributes
            Args:
            size (int): The size of the squar
            '''
    def __init__(self, size):
        self.__size = size
