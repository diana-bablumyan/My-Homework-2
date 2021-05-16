class Cube:

	def __init__(self, height, width, length):
		
		self.height = height
		self.width = width
		self.length = length

	def sorted_list(self):

		dim_tuple = (self.height, self.width, self.length)
		dim_list = list(dim_tuple).copy()
		dim_list.sort()
		return dim_list

	def __le__(self, other):

		if not isinstance(other, Cube):
			print("I can't compare different types")
			return False

		elif self.sorted_list()[0] <= other.sorted_list()[0] and self.sorted_list()[1] <= other.sorted_list()[1] and self.sorted_list()[2] <= other.sorted_list()[2]:
			print("First cube fit in second cube")
			return True

		else:
			print("First cube not fit in second cube")
			return False

cube1 = Cube(3, 9, 6) 
cube2 = Cube(8, 2, 7)
print("The answer is - ", cube1 <= cube2)
