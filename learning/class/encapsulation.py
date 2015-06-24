"""
Encapsulation:
1. First of the three pillars of OOP.
2. Encapsulation refers to the safe storage of data (attributes) in an instance.
	a. Data should be accessed through instance methods
	b. Data should be validated as correct depending on the prerequisites of the class.
	c. Data should be safe from changes by external process.
3. Summary: Setting the value in the object with the use of the setter method shown below is called Encapsulation.
""" 

#----------------- Example 1 ---------------------

class Class(object):

	def given_value(self, val):
		self.value = val

	def return_value(self):
		return self.value

inst1 = Class()
inst1.given_value("wccalvin")
print inst1.return_value()

inst2 = Class()
inst2.given_value("hello")
print inst2.return_value()

# Changing the value of second instance from outside the class or in the main body of the code
inst2.value = "***Hello World!***"
print inst2.return_value()


#----------------- Example 2 ----------------------

class Integer(object):

	def set_value(self, value):
		try:
			value = int(value)
		except ValueError:
			return
		self.value = value

	def get_value(self):
		return self.value

	def increment(self):
		return "Increment value by 10: {}".format(self.value + 10)

int_inst = Integer()
int_inst.set_value(5)
print "Assigned value: {}".format(int_inst.get_value())
print "Assigned value incremented by 10: {}".format(int_inst.increment())

# Break the code by assigning a string value instead of integer.
int_inst.value = "String"
print "Assigned value incremented by 10: {}".format(int_inst.increment())

