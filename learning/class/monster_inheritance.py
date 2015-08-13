from random import randint, choice

COLORS = ["yellow", "red", "brown", "blue", "black", "green"]

class Monster:

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

	def battlecry(self):
		return self.sound.upper()


print "-"*5, " About a Bird! ", "-"*5
bird = Monster(sound="tweet", color="blue", weapon="beak")
print bird.color
print bird.hit_points
print bird.weapon
print bird.battlecry()

print "-"*5, " About a Lion! ", "-"*5
lion = Monster(color="brown", weapon="teeth", hit_points=5)
print lion.color
print lion.hit_points
print lion.weapon
print lion.battlecry()


print "-"*5, " About a Warrior! ", "-"*5
man = Monster(hit_points=10)
print man.color
print man.hit_points
print man.weapon
print man.battlecry()

# Because of the set attribute method, we can set new variables - see below:

print "-"*5, " About a Dove! ", "-"*5
dove = Monster(color="white", weapon="patience", action="fly", sound="tawtee", hit_points=25)
print dove.color
print dove.hit_points
print dove.weapon
print dove.battlecry()
print dove.action

