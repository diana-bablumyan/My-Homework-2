class Circle:

	def __init__(self, radius):

		self.radius = radius
		self.p = 3.14

	def are(self):

		are	= self.radius ** 2 * self.p
		return are

	def perimeter(self):

		perimeter = self.radius * self.p
		return perimeter

radius_1 = Circle(2)
print(radius_1.are())
print(Circle.perimeter(radius_1))
