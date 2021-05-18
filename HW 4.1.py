###Check in "SSS Theorem", if we have tree sides###
class Triangle:

	def __init__(self, side1, side2, side3):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3

	def sorted_sides(self):

		sides_tuple = (self.side1, self.side2, self.side3)
		sides_list = list(sides_tuple).copy()
		sides_list.sort()
		return sides_list

	def __eq__(self, other):

		if not isinstance(other, Triangle):
			print("I can't compare different types")
			return False
		else:
			self_sides = self.sorted_sides()
			other_sides = other.sorted_sides()

			if self_sides[0] / other_sides[0] == self_sides[1] / other_sides[1] == self_sides[2] / other_sides[2]:
				return True
			else:
				return False

triangle1 = Triangle(7, 10, 4)
triangle2 = Triangle(20, 8, 14)
# print("Return true, when triangles are similar")
# print("Answer is -", triangle1 == triangle2)

###Check in "SAS Theorem", if we have two sides and one angle###
class Triangle:

	def __init__(self, side1, side2, angle):
		self.side1 = side1
		self.side2 = side2
		self.angle = angle

	def sorted_sides_angle(self):

			sides_angle_tuple = (self.side1, self.side2, self.angle)
			sides_angle_list = list(sides_angle_tuple).copy()
			sides_angle_list.sort()
			return sides_angle_list

	def __eq__(self, other):

		self_sides_angle = self.sorted_sides_angle()
		other_sides_angle = other.sorted_sides_angle()

		if not isinstance(other, Triangle):
			print("I can't compare different types")
			return False
		else:
			if self_sides_angle[0] / other_sides_angle[0] == self_sides_angle[1] / other_sides_angle[1] and self_sides_angle[2] == other_sides_angle[2]:
				return True
			else:
				return False

triangle1 = Triangle(30, 10, 12)
triangle2 = Triangle(5, 4, 30)
# print("Return true, when triangles are similar")
# print("Answer is -", triangle1 == triangle2)

###Check in "AA Theorem", if we have two angles###
class Triangle:

	def __init__(self, angle1, angle2):
		self.angle1 = angle1
		self.angle2 = angle2

	def sorted_angles(self):

			angles_tuple = (self.angle1, self.angle2)
			angles_list = list(angles_tuple).copy()
			angles_list.sort()
			return angles_list

	def __eq__(self, other):

		self_angles = self.sorted_angles()
		other_angles = other.sorted_angles()

		if not isinstance(other, Triangle):
			print("I can't compare different types")
			return False
		else:
			if (self_angles[0] == other_angles[0] and self_angles[1] == other_angles[1]):
				return True
			else:
				return False

triangle1 = Triangle(60, 20)
triangle2 = Triangle(60, 20)
print("Return true, when triangles are similar")
print("Answer is -", triangle1 == triangle2)