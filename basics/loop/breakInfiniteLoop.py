#!/usr/bin/env python

"""
Description: break statement breaks out of the while loop early
"""


number = 0
while True:
    number += 1
    if number == 100:
        print("Counted to {}!".format(number))
        break
