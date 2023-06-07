#!/usr/bin/python3

def print_last_digit(n):
    a = n % 10
    if n < 0:
        a = 10 - a
    print("{}".format(a), end="")
    return a
