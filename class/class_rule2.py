"""
RULE 2: Variables defined in the class are available to the instance.
"""


class MyClass(object):
    """Adding sample documentation for example"""
    var = "Class variable is available!"

first_obj = MyClass()
print first_obj.var

second_obj = MyClass()
print second_obj.var


print(second_obj.__doc__)
