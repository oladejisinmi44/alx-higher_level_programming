#!/usr/bin/python3

a = 122
for i in range(97, 123):
    if (a % 2 == 1):
        b = a - 32
    else:
        b = a
    print("{}".format(chr(b)), end="")
    a = a - 1
