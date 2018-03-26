class NewClass:  # class
    name = 'Clayton'  # attribute

    def name_method(self):  # method
        return self.name


new_instance = NewClass()  # instance of a class

# It has access to all the attributes and methods
print new_instance.name  # attribute
print new_instance.name_method()  # method
