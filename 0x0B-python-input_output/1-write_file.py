#!/usr/bin/python3
"""
This module supplies the function "write_file".
"""


def write_file(filename="", text=""):
    """
    This function writes to a file.
    """
    with open(filename, mode="w", encoding="UTF-8") as fd:
        a = fd.write(text)
    return a
