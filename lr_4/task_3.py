import math

class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def distance_from_origin_to_point(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def distance_from_point_to_point(self, point_x, point_y):
        return math.sqrt((point_x - self.x)**2 + (point_y - self.y)**2)
    
    def distance_from_point_to_line(self, a, b, c):
        return abs(a * self.x + b * self.y + c) / math.sqrt(a**2 + b**2)
    
point_1 = Point(15, 4)
print(f"расстояние от начала координат до точки: {point_1.distance_from_origin_to_point()}")
print(f"расстояние от точки до точки: {point_1.distance_from_point_to_point(12, 15)}")
print(f"расстояние от точки до прямой: {point_1.distance_from_point_to_line(9, 2, 8)}")