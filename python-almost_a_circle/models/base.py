#!/usr/bin/python3
"""class """


class Base:
    """
    This is the base class that manages the id attribute
    for all other classes in the project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
