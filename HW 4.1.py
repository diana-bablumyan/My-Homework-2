###Check in "SSS Theorem", if we have tree sides###
class Triangle:

	def __init__(self, side1, side2, side3):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3

	def __eq__(self, other):

		if not isinstance(other, Triangle):
			print("I can't compare different types")
			return False
		else:
			if self.side1 / other.side1 == self.side2 / other.side2 == self.side3 / other.side3:
				return True
			else:
				return False

triangle1 = Triangle(20, 10, 4)
triangle2 = Triangle(10, 5, 2)
# print("Return true, when triangles are similar")
# print("Answer is -", triangle1 == triangle2)

###Check in "SAS Theorem", if we have two sides and one angle###
class Triangle:

	def __init__(self, side1, side2, angle):
		self.side1 = side1
		self.side2 = side2
		self.angle = angle

	def __eq__(self, other):

		if not isinstance(other, Triangle):
			print("I can't compare different types")
			return False
		else:
			if self.side1 / other.side1 == self.side2 / other.side2 and self.angle == other.angle:
				return True
			else:
				return False

triangle1 = Triangle(20, 10, 30)
triangle2 = Triangle(10, 5, 30)
# print("Return true, when triangles are similar")
# print("Answer is -", triangle1 == triangle2)

###Check in "AA Theorem", if we have two angles###
class Triangle:

	def __init__(self, angle1, angle2):
		self.angle1 = angle1
		self.angle2 = angle2

	def __eq__(self, other):

		if not isinstance(other, Triangle):
			print("I can't compare different types")
			return False
		else:
			if (self.angle1 == other.angle1 and self.angle2 == other.angle2) or (self.angle1 == other.angle2 and self.angle2 == other.angle1):
				return True
			else:
				return False

triangle1 = Triangle(20, 60)
triangle2 = Triangle(60, 20)
print("Return true, when triangles are similar")
print("Answer is -", triangle1 == triangle2)