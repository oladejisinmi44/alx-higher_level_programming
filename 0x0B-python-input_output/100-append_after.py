#!/usr/bin/python3
"""
This module provides the function "append_after".
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This is a  function that inserts a line of text to a
    file, after each line containing a specific string.
    """
    if len(filename) == 0 or len(search_string) == 0:
        return
    file_cont = []
    with open(filename, 'r+', encoding="UTF-8") as fd:
        file_cont = fd.readlines()
    with open(filename, 'w', encoding="UTF-8") as fd:
        fd.write(file_cont[0])
    i = 0
    for a in file_cont:
        if search_string in a:
            file_cont.insert(i + 1, new_string)
        i += 1
    with open(filename, 'a', encoding="UTF-8") as fd:
        for b in range(1, len(file_cont)):
            fd.write(file_cont[b])
