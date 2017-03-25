#!/usr/local/bin/python3


class Greeter(object):

    def hello(self):
        print("Hello!")

    def goodbye(self):
        print("Good Bye...")

inst = Greeter()  # Creates instance for the class

inst.hello()  # Invoke hello method in the class
inst.goodbye()  # Invoke goodbye method in the class
