import random


class Dice(object):

	def __init__(self, sides):
		self.sides = sides

	def roll(self):
		return random.randint(1, self.sides)


game1 = Dice(12)

print game1.roll()
print game1.roll()
print game1.roll()

game2 = Dice(20)
print game2.roll()
print game2.roll()
print game2.roll()
