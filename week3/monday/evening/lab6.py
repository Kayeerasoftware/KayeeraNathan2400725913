from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


rectangle = Rectangle(10, 5)
circle = Circle(7)

print("RECTANGLE")
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")

print("\nCIRCLE")
print(f"Area: {circle.area():.2f}")
print(f"Perimeter: {circle.perimeter():.2f}")