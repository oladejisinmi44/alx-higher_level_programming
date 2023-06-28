#!/usr/bin/python3

"""
This is the "Square"  module.
This module provides a simple Square class defined by size "size"
which is a private instance attribute that
must be an integer not less than or equal to zero.
"""


class Square:
    """
    Square:
    Class used to define a square with size "size".
    """
    def __init__(self, size=0):
        """
        __init__:
        Function to initialize object
        Args:
        self: Instance of object
        size: size of square(private instance attribute)
        which must be an integer not less than or equal to zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        area: returns area of square
        Args:
        self: Instance of object
        Return: area of square object
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        size: getter function to access private instance attribute "size".
        Args:
        self: instance of object
        Return: the size attribute
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        size: setter function for private instance attribute "size"
        Args:
        self: instance of object
        size: intended size to set
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def my_print(self):
        x = self.__size
        if x == 0:
            print("")
            return
        for i in range(x):
            print("#" * x)
