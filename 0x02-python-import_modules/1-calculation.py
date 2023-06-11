#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    u = add(a, b)
    print("{} + {} = {}".format(a, b, u))
    v = sub(a, b)
    print("{} - {} = {}".format(a, b, v))
    w = mul(a, b)
    print("{} * {} = {}".format(a, b, w))
    x = div(a, b)
    print("{} / {} = {}".format(a, b, x))
