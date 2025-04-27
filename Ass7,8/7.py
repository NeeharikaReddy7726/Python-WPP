import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def rotation_with_respect_to_x(self):
        return math.degrees(math.atan2(self.y, self.x))

    @staticmethod
    def distance(v1, v2):
        return math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2)

    @staticmethod
    def dot_product(v1, v2):
        return v1.x * v2.x + v1.y * v2.y

    @staticmethod
    def cross_product(v1, v2):
        return v1.x * v2.y - v1.y * v2.x

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

def main_2d():
    print("2-D Vector Operations")
    x1 = float(input("Enter the x-coordinate of vector 1: "))
    y1 = float(input("Enter the y-coordinate of vector 1: "))
    v1 = Vector2D(x1, y1)
    
    x2 = float(input("Enter the x-coordinate of vector 2: "))
    y2 = float(input("Enter the y-coordinate of vector 2: "))
    v2 = Vector2D(x2, y2)

    print(f"Vector1: {v1}")
    print(f"Vector2: {v2}")
    print(f"Magnitude of Vector1: {v1.magnitude()}")
    print(f"Rotation of Vector1 with respect to X-axis: {v1.rotation_with_respect_to_x()} degrees")
    print(f"Distance between Vector1 and Vector2: {Vector2D.distance(v1, v2)}")
    print(f"Dot product of Vector1 and Vector2: {Vector2D.dot_product(v1, v2)}")
    print(f"Cross product of Vector1 and Vector2: {Vector2D.cross_product(v1, v2)}")

main_2d()
