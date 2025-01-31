from abc import ABC, abstractmethod
import math

# Base class for all shapes (Abstraction + Encapsulation)
class Shape(ABC):
    def __init__(self, name):
        self.name = name  # Encapsulation: Protected attribute
        print(f"Creating a shape: {self.name}")

    @abstractmethod
    def area(self):
        pass  # Abstract method to enforce that all subclasses must implement this method
    
    @abstractmethod
    def perimeter(self):
        pass  # Abstract method to enforce that all subclasses must implement this method
    
    def __str__(self):
        return f"{self.name} (Area: {self.area()}, Perimeter: {self.perimeter()})"


# Circle class (Inheritance + Polymorphism)
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")  # Calling the constructor of the parent (Shape) class
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Rectangle class (Inheritance + Polymorphism)
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Triangle class (Inheritance + Polymorphism)
class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a  # Side A
        self.b = b  # Side B
        self.c = c  # Side C

    def area(self):
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# Test functionality
if __name__ == "__main__":
    # Creating instances of different shapes
    circle = Circle(5)
    print(circle)

    rectangle = Rectangle(4, 6)
    print(rectangle)

    triangle = Triangle(3, 4, 5)
    print(triangle)
