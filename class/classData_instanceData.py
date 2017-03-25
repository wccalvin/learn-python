"""
1. An instance can access class data.
2. Class data is the data which is intended to be shared among instances.
"""
import format

class InstanceCounter(object):
	count = 0

	def __init__(self, num1):
		self.value = num1
		InstanceCounter.count += 1 # Yes, we can call class attribute inside the method as shown.

	def set(self, num2):
		self.given = self.num2

	def get(self):
		return self.given

	def counter(self):
		return InstanceCounter.count


format.example("-", 1, 7)

# create 5 difference instances
inst_1 = InstanceCounter(2)
print "Class Data   : %s"%inst_1.count # This eventually changes to 5 because the count is incremented as new instances are created.
inst_2 = InstanceCounter(4)
print "Class Data   : %s"%inst_2.count # This eventually changes to 5 because the count is incremented as new instances are created.
inst_3 = InstanceCounter(6)
print "Class Data   : %s"%inst_3.count # This eventually changes to 5 because the count is incremented as new instances are created.
inst_4 = InstanceCounter(8)
print "Class Data   : %s"%inst_4.count # This eventually changes to 5 because the count is incremented as new instances are created.
inst_5 = InstanceCounter(10)
print "Class Data   : %s"%inst_5.count # This eventually changes to 5 because the count is incremented as new instances are created.

print "Class Data of inst_1: %s"%inst_1.count # This eventually changes to 5 because the count is incremented as new instances are created.
print "Instance Data: %s"%inst_3.value

format.example("-", 2, 7)
(inst_1.given, inst_2.given, inst_3.given, inst_4.given, inst_5.given) = (15, 30, 45, 60, 75)
for i in (inst_1, inst_2, inst_3, inst_4, inst_5):
	print "Given Value   : %s"%i.get()
	print "Instance Count: %s"%i.counter()
