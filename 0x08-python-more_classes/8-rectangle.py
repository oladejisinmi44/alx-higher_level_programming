#!/usr/bin/python3
"""
This is a module that supplies the class "rectangle".
"""


class Rectangle:
    """
    This is a class that initiates a rectangle object.
    It has a private instance attributes "height" and "width" which
    must be integers.
    It has public instance methods "area" for calculating the recangle's
    area and "perimeter" for calculating it's perimeter.
    It also has public class attributes "number_of_instances"
    which counts the number of instances that exist and "print_symbol"
    which contains a string used to represent the rectangle.
    Here, there is a static method "bigger_or_equal" to return the
    bigger rectangle based on the area.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        return (2 * (self.__height + self.__width))

    def __str__(self):
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return(rect)
        for i in range(self.__height):
            for j in range(self.__width):
                rect += str(self.print_symbol)
            if i < self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
