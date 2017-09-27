import random


class Thief:
    sneaky = True

    def pickpocket(self):
        if self.sneaky:
            return bool(random.randint(0, 1))


thief_instance = Thief()
print thief_instance.pickpocket()

thief_instance.sneaky = False
print thief_instance.pickpocket()
