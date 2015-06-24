"""RULE 4: Instance have their own data, instance attributes."""

from random import randint

class MyClass(object):
	
	var_stable    = 5

	def dothis(self):
		self.rand_val = randint(25, 50)

myInst1 = MyClass()
myInst1.dothis()

myInst2 = MyClass()
myInst2.dothis()

print "First instance: %s"%myInst1
print "Unchanged data from first instance : ", myInst1.var_stable
print "Changeable data from first instance: ", myInst2.rand_val


print "Second instance: %s"%myInst2
print "Unchanged data from second instance : ", myInst1.var_stable
print "Changeable data from second instance: ", myInst2.rand_val

# To experiment run this code few times.
