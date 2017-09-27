class NewClass:
    name = 'Clayton'

    def name_method(self):
        return self.name

new_instance = NewClass()
name = new_instance.name_method()
print name
