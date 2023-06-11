#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    lag = len(argv)
    if lag - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        o = argv[2]
        if o == "+":
            d = add(a, b)
        elif o == "-":
            d = sub(a, b)
        elif o == "*":
            d = mul(a, b)
        elif o == "/":
            d = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{} {} {} = {}".format(a, o, b, d))
