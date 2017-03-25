"""
RULE 2: Variables defined in the class are available to the instance.
"""


class MyClass(object):
    var = "Class variable is available!"

first_obj = MyClass()
print first_obj.var

second_obj = MyClass()
print second_obj.var
