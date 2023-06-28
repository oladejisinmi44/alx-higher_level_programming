#!/usr/bin/python3

"""
This is the "Square"  module.
This module provides a simple Square class defined by size "size"
which must be an integer not less than or equal to zero.
"""


class Square:
    """
    Square:
    Class used to define a sqquare with size "size".
    """
    def __init__(self, size=0):
        """
        __init__:
        Function to initialize object
        Args:
        self: Instance of object
        size: Size of square
        which must be an integer not less than or equal to zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
