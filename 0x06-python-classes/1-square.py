#!/usr/bin/python3

"""
This is the "Square"  module.
This module provides a simple Square class.
"""


class Square:
    """
    Square:
    Class used to define a sqquare with size "size".
    """
    def __init__(self, size):
        """
        __init__:
        Function to initialize object
        Args:
        self: Instance of object
        size: Size of square
        """
        self.__size = size
