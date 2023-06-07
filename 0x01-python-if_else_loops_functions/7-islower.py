#!/usr/bin/python3

def islower(alph):
    i = ord(alph)
    if (i >= 97) and (i <= 122):
        return True
    elif (i >= 65) and (i <= 90):
        return False
