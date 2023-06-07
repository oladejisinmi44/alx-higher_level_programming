#!/usr/bin/python3

def remove_char_at(str, n):
    if (str == ""):
        return ""
    cp = str
    if (n < 0):
        return cp
    if (n == 0):
        cp = cp[1:]
    elif (n == -1):
        cp = cp[:-1]
    else:
        cp1 = cp[:n]
        cp2 = cp[n + 1:]
        cp = cp1 + cp2
    return cp
