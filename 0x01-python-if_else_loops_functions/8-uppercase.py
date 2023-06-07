#!/usr/bin/python3

def uppercase(sstr):
    c = len(sstr)
    word = ""
    if (c != 1) and (c != 0):
        for a in range(0, c):
            b = ord(sstr[a])
            if (b >= 97) and (b <= 122):
                b = b - 32
            word = word + chr(b)
    elif (c == 1):
        b = ord(sstr[0])
        if (b >= 97) and (b <= 122):
            b = b - 32
        word = chr(b)
    print("{}".format(word), end="")
    print("")
