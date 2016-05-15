class Character(object):
	experience = 0
	hit_points = 10

	def get_weapon(self):
		weapon_choice = raw_input("Weapon ([S]word, [A]xe, [B]ow): ").lower()

		if weapon_choice in 'sab':
			if weapon_choice == 's':
				return "sword"
			if weapon_choice == 'a':
				return "axe"
			if weapon_choice == 'b':
				return "bow"
		else:
			self.get_weapon()


	# To update the values the below method is used
	def __init__(self, **kwargs):
		self.name = raw_input("Name: ")
		self.weapon = self.get_weapon()

		for key, value in kwargs.items():
			setattr(self, key, value)



player = Character()
print player.weapon
print player.name
