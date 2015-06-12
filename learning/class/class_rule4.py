"""RULE 4: Instance have their own data, instance attributes."""

from random import randint

class MyClass(object):
	
	var_stable    = 5

	def dothis(self):
		self.rand_val = randint(25, 50)

myInst = MyClass()
myInst.dothis()

print "Unchanged data: ", myInst.var_stable

print "Changeable data: ", myInst.rand_val

# To experiment run this code few times.
