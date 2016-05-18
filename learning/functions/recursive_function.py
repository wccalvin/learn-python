#!/usr/bin/env python


def myFunction(num):
    if num == 0:
        return True
    else:
        print(num)
        myFunction(num=num - 1)

myFunction(10)
