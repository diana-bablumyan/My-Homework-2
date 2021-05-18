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

		self_dim = self.sorted_list()
		other_dim = other.sorted_list()


		if not isinstance(other, Cube):
			print("I can't compare different types")
			return False

		elif self_dim[0] <= other_dim[0] and self_dim[1] <= other_dim[1] and self_dim[2] <= other_dim[2]:
			print("First cube fit in second cube")
			return True

		else:
			print("First cube not fit in second cube")
			return False

cube1 = Cube(3, 5, 6) 
cube2 = Cube(8, 4, 7)
print("The answer is - ", cube1 <= cube2)
