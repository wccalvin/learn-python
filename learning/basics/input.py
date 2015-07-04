# Difference between raw_input() and input():
# input() evaluates the input as python code (whether it is string or integer or float)
# raw_input() assumes your input as string.

name = input("Enter an input? Note: Using input():\n")
print type(name)
print "Your name is: %s"%name

name = raw_input("Enter an input? Note: Using raw_input():\n")
print type(name)
print "Your name is: %s"%name
