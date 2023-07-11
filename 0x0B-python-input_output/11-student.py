#!/usr/bin/python3
"""
This module supplies the class "student".
"""


class Student:
    """
    Student class.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        dictt = {}
        for a in attrs:
            if a in self.__dict__:
                dictt[a] = self.__dict__[a]
        return dictt

    def reload_from_json(self, json):
        for i, j in json.items():
            if i == "first_name":
                self.first_name = j
            elif i == "last_name":
                self.last_name = j
            elif i == "age":
                self.age = j
