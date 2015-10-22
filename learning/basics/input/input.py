__author__ = 'wccalvin'

# Difference between raw_input() and input():
# input() evaluates the input as python code (whether it is string or integer or float)
# This means, if you are typing string as input, you should use the quote marks.
# raw_input() assumes your input as string.

name = input("Enter an input? Note: Using input():\n")
print(type(name))
print("Your name is: {}".format(name))

name = raw_input("Enter an input? Note: Using raw_input():\n")
print(type(name))
print("Your name is: {}".format(name))



# -------------------------------------------
# Sample output (string):
# -------------------------------------------
# C:\Python27\python.exe D:/users/vwj/do_not_delete/py/learning/basics/input.py
# Enter an input? Note: Using input():
# "Clayton"
# <type 'str'>
# Your name is: Clayton
# Enter an input? Note: Using raw_input():
# Clayton
# <type 'str'>
# Your name is: Clayton
# -------------------------------------------

# -------------------------------------------
# Sample output (integer):
# -------------------------------------------
# -------------------------------------------
# Sample output (string):
# -------------------------------------------
# Enter an input? Note: Using input():
# 56
# <type 'int'>
# Your name is: 56
# Enter an input? Note: Using raw_input():
# 56
# <type 'str'>
# Your name is: 56
# -------------------------------------------
# -------------------------------------------