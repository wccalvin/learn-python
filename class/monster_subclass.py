from random import randint, choice

COLORS = ["yellow", "red", "brown", "blue", "black", "green"]

class Monster(object):

	min_hit_points = 1
	max_hit_points = 1
	min_experience = 1
	max_experience = 1
	weapon         = "sword"
	sound          = "roar"

	def __init__(self, **kwargs):
		self.hit_points = randint(self.min_hit_points, self.max_hit_points)
		self.experience = randint(self.min_experience, self.max_experience)
		self.color      = choice(COLORS)

		for key, value in kwargs.items():
			setattr(self, key, value)

	# This method changes our classes to become strings
	# Try printing the class without this method below
	def __str__(self):
		return "{} {} with Hit Points: {}".format(self.color.title(),
											  self.__class__.__name__,
											  self.hit_points)

	def battlecry(self):
		return self.sound.upper()


class Goblin(Monster):

	max_hit_points = 3
	max_experience = 2
	sound          = "squeak"	


class Troll(Monster):
	min_hit_points = 3
	max_hit_points = 5
	min_experience = 2
	max_experience = 6
	sound          = "growl"


class Dragon(Monster):
	min_hit_points = 5
	max_hit_points = 10
	min_experience = 6
	max_experience = 10
	sound          = "raaaaaaaaaar"


azog  = Goblin()
snaga = Troll()
pete  = Dragon()

print pete.hit_points
print snaga.battlecry()
print azog.sound

print pete # Try this after commenting out the __str__ method above
