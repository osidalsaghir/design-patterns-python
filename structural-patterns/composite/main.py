from abc import ABC, abstractmethod

# Component (Common interface for leaf and composite objects)
class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass

# Leaf (Individual graphic objects)
class Line(Graphic):
    def __init__(self, name):
        self.name = name

    def draw(self):
        return f"Drawing Line: {self.name}"

class Circle(Graphic):
    def __init__(self, name):
        self.name = name

    def draw(self):
        return f"Drawing Circle: {self.name}"

# Composite (Composite graphic objects)
class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)

    def draw(self):
        results = []
        for graphic in self.graphics:
            results.append(graphic.draw())
        return "\n".join(results)

# Client code
if __name__ == "__main__":
    line1 = Line("Line 1")
    line2 = Line("Line 2")
    circle1 = Circle("Circle 1")
    circle2 = Circle("Circle 2")

    composite = CompositeGraphic()
    composite.add(line1)
    composite.add(line2)
    composite.add(circle1)

    composite_group = CompositeGraphic()
    composite_group.add(composite)
    composite_group.add(circle2)

    print("Drawing all graphics:")
    print(composite_group.draw())
