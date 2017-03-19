#!/usr/bin/env python

import sys

"""
Example depicts a recursive funtion. The function which has a potential to call
itself.
"""


def rfunc(num):
    if num < 0:
        print("Can't use a negative value.")
    elif num == 0:
        return True
    else:
        print(num)
        rfunc(num-1)


if __name__ == '__main__':
    try:
        number = input("Enter an integer: ")
        try:
            number = int(number)
            rfunc(number)
        except ValueError:
            print("You've entered a string.")
            print("Try again with an integer.")
            sys.exit(1)
    except NameError:
        print("Not an integer. Try again.")
        sys.exit(1)
