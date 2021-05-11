class Shape:

    def __init__(self, name):

        self.name = name

    def present_shape(self):
        
        return f"The name of shape is {self.name}"


class Triangle(Shape):

    def __init__(self, name, side1, side2, base, height):

        self.side1 = side1
        self.side2 = side2
        self.base = base
        self.height = height

        super().__init__(name)

    def present(self):
        return F"{self.present_shape()}, 1st side: {self.side1}, 2nd: {self.side2}, base: {self.base} and height: {self.height}"

    def area(self):

        area = 1/2 * self.base * self.height
        return f"Area: {area}"

    def perimeter(self):

        perimeter = self.base + self.side1 + self.side2
        return f"Perimeter: {perimeter}"
        

class Square(Shape):
    
    def __init__(self, name, side):

        self.side = side
    
        super().__init__(name)

    def present(self):
        return f"{self.present_shape()}, sides are equal to {self.side}"

    def area(self):
        return f"The area: {self.side ** 2}"

    def perimeter(self):
        return f"The perimeter: {self.side * 4}"

    def diagonal(self):
        return f"The diagonal: {self.side * (2 ** 1/2)}"


shape_1 = Shape("square")
print(shape_1.present_shape())
print("----------")

triangle_1 = Triangle("triangle", 2, 3, 5, 4)
print("Triangle characteristics")
print(triangle_1.present())
print(triangle_1.area())
print(triangle_1.perimeter())
print("----------")

square_1 = Square("square", 4)
print("Square characteristics")
print(square_1.present())
print(square_1.area())
print(square_1.perimeter())
print(square_1.diagonal())

