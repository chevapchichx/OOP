import math

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return (self.width + self.length) * 2
    
    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.length**2)


rectangle_1 = Rectangle(5, 2)
rectangle_2 = Rectangle(10, 30)

print(f"площадь 1 прямоугольника: {rectangle_1.area()}, периметр 1 прямоугольника: {rectangle_1.perimeter()}")
print(f"площадь 2 прямоугольника: {rectangle_2.area()}, периметр 2 прямоугольника: {rectangle_2.perimeter()}")