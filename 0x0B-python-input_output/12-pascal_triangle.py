#!/usr/bin/python3
"""
This module supplies the function "pascal_triangle".
"""


def pascal_triangle(n):
    """
    This is a function that returns a list of lists of
    integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    pt = [[1]]
    for a in range(n - 1):
        new = [1]
        itr = pt[-1]
        for i in range(len(pt[-1]) - 1):
            new.append(itr[i] + itr[i + 1])
        new.append(1)
        pt.append(new)
    return pt
