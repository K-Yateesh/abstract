from abc import ABC, abstractmethod
import math

# =========================
# Abstract Base Class
# =========================
class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


# =========================
# Circle Class
# =========================
class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"


# =========================
# Rectangle Class
# =========================
class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and Height must be positive")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


# =========================
# Triangle Class
# =========================
class Triangle(Shape):
    def __init__(self, a, b, c):
        # Validate triangle inequality
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def area(self) -> float:
        # Heron's Formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def __str__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"


# =========================
# Function for Total Metrics
# =========================
def total_metrics(shapes: list[Shape]) -> tuple[float, float]:
    total_area = sum(shape.area() for shape in shapes)
    total_perimeter = sum(shape.perimeter() for shape in shapes)
    return total_area, total_perimeter


# =========================
# Demonstration (Polymorphism)
# =========================
if __name__ == "__main__":
    shapes = [
        Circle(2.5),
        Rectangle(4, 6),
        Triangle(3, 4, 5)
    ]

    print("Shapes:")
    for shape in shapes:
        print(shape)

    total_area, total_perimeter = total_metrics(shapes)

    print("\nTotal Area:", total_area)
    print("Total Perimeter:", total_perimeter)