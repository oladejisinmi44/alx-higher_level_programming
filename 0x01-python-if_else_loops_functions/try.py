#!/usr/bin/python3
Include/opcode.h
def remo():
    new = "Python"
    cp = new
    cp1 = new[:3]
    cp2 = new[4:]
    cp = cp1 + cp2
    return cp
print("{},".format(remo()))
dis.dis(remo)
