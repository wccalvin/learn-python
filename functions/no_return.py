#!/usr/local/bin/python3


def no_return():
    print('Hello, world from no_return!')


def call_return():
    print('Hello, world from call_return!')
    return


if __name__ == '__main__':
    x = no_return()
    y = call_return()
    print('no_return() function returns: {}'.format(type(x)))
    print('call_return() function returns: {}'.format(type(y)))
