#!/usr/bin/env python


def addition(num1, num2):
    """returns the sum of two numbers."""
    return num1 + num2


def difference(num1, num2):
    """returns the difference between two numbers."""
    return num1 - num2


def square(num):
    """returns the square of given number"""
    return num**2


if __name__ == '__main__':
    print(addition(20, 5))
    print(difference(10, 5))
    print(square(5))
    print(addition(2016, 34) + difference(575, 324) - square(15))
