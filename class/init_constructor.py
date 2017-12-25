#!/usr/local/bin/python2
"""
It is a special method that allows to initialize attributes at the time an instance is constructed.
"""
import format

class NumberIncrement(object):

    def __init__(self, value):
        try:
            number = int(value)
        except ValueError:
            number = 0
        self.number = number

    def increment(self):
        self.incremented_value = self.number + 1

#-------------Example 1 --------------
format.example("-", 1, 5)
ins1 = NumberIncrement(5)
ins1.increment()
print ins1.incremented_value
format.end("-", 11)

#-------------Example 2 --------------
format.example("-", 2, 5)
ins2 = NumberIncrement("string")
ins2.increment()
print ins2.incremented_value
format.end("-", 11)
