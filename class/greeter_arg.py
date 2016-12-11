class Greeter(object):

	def __init__(self, name):
		self.name = name
	
	def hello(self):
		print "Hello {}!".format(self.name)

	def goodbye(self):
		print "Good bye {}.".format(self.name)

inst1 = Greeter("foo") # Creates instance for the class

inst1.hello() # Invoke hello method in the class
inst1.goodbye() # Invoke goodbye method in the class

inst2 = Greeter("bar")

inst2.hello()
inst2.goodbye()
