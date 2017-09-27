"""
RULE 3: A method on an instance passes instance as the first argument to the
method. (named self in the method)
"""


class MyClass(object):

    def callme(self):
        return self  # This is added to experiment.


myInst = MyClass()

# To prove that instance is passed as first argument,
#   1. Add print self to the method.
#   2. print the myInst.
# Both should refer to the same hex value.

print myInst.callme()  # Calling the method inside the class
print myInst  # Calling the instance of the class
