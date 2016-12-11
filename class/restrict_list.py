class MaxSizeList(object):

	complete_list = []

	def __init__(self, max):
		self.limit = max

	def push(self, elements):
		self.value = elements
		MaxSizeList.complete_list.append(self.value)

	def get_list(self):
		self.final = MaxSizeList.complete_list[-self.limit:]
		return self.final

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("how")
a.push("are")
a.push("you")
a.push("doing")

b.push("how")
b.push("are")
b.push("you")
b.push("doing")

print a.get_list()
print b.get_list()
