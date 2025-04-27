import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

def main():
    shape_type = input("Enter the shape (rectangle/circle): ").lower()
    if shape_type == "rectangle":
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        rect = Rectangle(width, height)
        print(f"Rectangle - Area: {rect.area()}, Perimeter: {rect.perimeter()}")
    elif shape_type == "circle":
        radius = float(input("Enter the radius of the circle: "))
        circ = Circle(radius)
        print(f"Circle - Area: {circ.area()}, Perimeter: {circ.perimeter()}")
    else:
        print("Invalid shape type!")

if __name__ == "__main__":
    main()
