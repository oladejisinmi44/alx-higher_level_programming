#!/usr/bin/python3
""" base """

class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize class"""
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects 