"""RULE 1: An instance of a class knows what class its from."""

class MyClass(object):
	pass

# Creating two instances to prove the theory that they are independant!

MyInst1 = MyClass()
print MyInst1

MyInst2 = MyClass()
print MyInst2
