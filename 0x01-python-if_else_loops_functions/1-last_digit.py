#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = number % 10
if number < 0:
    a -= 10
stl = "Last digit of"
if a > 5:
    print("{} {} is {} and is greater than 5".format(stl, number, a))
elif a == 0:
    print("{} {} is {} and is 0".format(stl, number, a))
elif (a < 6) and (a != 0):
    print("{} {} is {} and is less than 6 and not 0".format(stl, number, a))
