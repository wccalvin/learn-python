import random


# Below code to understand self
class Thief:
    sneaky = True

    def pickpocket(self):
        print self
        return bool(random.randint(0, 1))


thief_instance = Thief()
print thief_instance.pickpocket()

# another way to call the same method for the instance
Thief.pickpocket(thief_instance)
