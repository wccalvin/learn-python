#!/usr/local/bin/python3

"""
Class Attributes vs Instance Attributes

In the below,
    class_data is a class attribute.
    inst_data is an instance attribute.
"""

import format


class DataCheck(object):
    class_data = "This is class data!"

    def set(self):
        self.inst_data = "This is instance data!"

format.example("-", 1, 7)
check = DataCheck()
print(check.class_data)

check.set()
print(check.inst_data)

# Change the value of class_data
format.example("-", 2, 7)
check.class_data = "Changed value of class_data"
print(check.class_data)

# Change the value of inst_data
format.example("-", 3, 7)
check.inst_data = "Changed value of inst_data"
print(check.inst_data)

# Try delete for class_data
format.example("-", 4, 7)
del check.class_data
print(check.class_data)  # Reverts back to the original class data

# Try delete for inst_data
format.example("-", 5, 7)
del check.inst_data  # This instance data will be lost.

try:
    print(check.inst_data)
except AttributeError as e:
    print("Previous data is lost: %s".format(e))
