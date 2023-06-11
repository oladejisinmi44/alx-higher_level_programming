#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lag = len(argv)
    d = 0
    if lag == 1:
        print("0")
    else:
        for i in range(1, lag):
            d += int(argv[i])
        print("{}".format(d))
