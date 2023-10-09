# Abstraction
class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

# Concrete Abstraction
class Circle(Shape):
    def draw(self):
        return f"Drawing a Circle in {self.color} color"

class Square(Shape):
    def draw(self):
        return f"Drawing a Square in {self.color} color"

# Implementation
class Color:
    def fill(self):
        pass

# Concrete Implementation
class RedColor(Color):
    def fill(self):
        return "Fill with red color"

class BlueColor(Color):
    def fill(self):
        return "Fill with blue color"

# Bridge
class Bridge:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def draw(self):
        return self.shape.draw()

    def fill(self):
        return self.color.fill()

# Client code
if __name__ == "__main__":
    red_circle = Bridge(Circle("Red"), RedColor())
    blue_square = Bridge(Square("Blue"), BlueColor())

    print(red_circle.draw())  # Output: Drawing a Circle in Red color
    print(red_circle.fill())  # Output: Fill with red color

    print(blue_square.draw())  # Output: Drawing a Square in Blue color
    print(blue_square.fill())  # Output: Fill with blue color
