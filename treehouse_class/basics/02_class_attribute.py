class Thief:
    sneaky = True

clayton = Thief()

# check whats in instance
print clayton

# can we just called the class and is it same as above instance?
print Thief()  # No, it is a different instance

# call the attribute of from instance
print clayton.sneaky

# call the attribute directly from class
print Thief().sneaky

# another way to do the above
print Thief.sneaky

# change the instance attribute value
clayton.sneaky = False
print clayton.sneaky

# can we change the attribute value directly in the class?
Thief.sneaky = False
print Thief.sneaky  # No, we can't.
