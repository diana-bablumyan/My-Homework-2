import random

class StrDict:

	def __init__(self, text):

		self.text = text
		self.dict = {}
		for i in text:
			self.dict[i] = random.randint(1,9)
		print(self.dict)

	def no_dupl(self):

		return set(self.dict.values())

	def tree_max(self):

		return sorted(list(self.dict.values()))[-3:]

	def present(self):

		return f"My given str input is {self.text}, the dictinory wich I get {self.dict}. Dict values without duplicate is {self.no_dupl()} and tree max values are {self.tree_max()}"





string_1 = StrDict("python")
print(string_1.no_dupl())
print(string_1.tree_max())
print(string_1.present())
