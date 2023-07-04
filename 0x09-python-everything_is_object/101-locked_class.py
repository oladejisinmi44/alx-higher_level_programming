#!/usr/bin/python3
"""
This is the module that supplies the class LockedClass
"""


class LockedClass:
    """
    Class for initializing LockedClass object.
    It prevents the user from dynamically creating new
    instance attributes, except if the new
    instance attribute is called first_name.
    """
    __slots__ = ['first_name']
