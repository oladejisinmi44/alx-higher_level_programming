#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    nag = len(argv)
    print("{} ".format(nag - 1), end="")
    if (nag - 1 == 1):
        print("argument:")
    else:
        print("arguments", end="")
        if (nag - 1 == 0):
            print(".")
        else:
            print(":")
    for i in range(1, nag):
        print("{}: {}".format(i, argv[i]))
