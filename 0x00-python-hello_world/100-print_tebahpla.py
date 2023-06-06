#!/usr/bin/python3

a = 122
for i in range(97, 123):
    if (a % 2 == 1):
        a = a - 32
    print("{}".format(chr(a)), end="")
