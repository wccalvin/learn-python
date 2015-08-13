
class Monster:

	def __init__(self, **kwargs):
		self.hit_points = kwargs.get("hit_points", 1)
		self.weapon     = kwargs.get("weapon", "sword")
		self.color      = kwargs.get("color", "yellow")
		self.sound      = kwargs.get("sound", "roar")

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
