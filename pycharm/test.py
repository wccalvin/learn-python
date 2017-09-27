#!/usr/bin/env python


def how_about_this():
    print "This is one way to go."


class Test:
    def __init__(self):
        self.first_name = 'Clayton'
        self.last_name = 'William'

if __name__ == '__main__':
    test_inst = Test()
    print type(test_inst)
    print test_inst.first_name
    print test_inst.last_name
