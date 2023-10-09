# Element interface
class Element:
    def accept(self, visitor):
        pass

# Concrete Element classes
class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_element_a(self)

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_element_b(self)

# Visitor interface
class Visitor:
    def visit_element_a(self, element_a):
        pass

    def visit_element_b(self, element_b):
        pass

# Concrete Visitor class
class ConcreteVisitor(Visitor):
    def visit_element_a(self, element_a):
        print("Visitor is processing ConcreteElementA")

    def visit_element_b(self, element_b):
        print("Visitor is processing ConcreteElementB")

# Object Structure class
class ObjectStructure:
    def __init__(self):
        self.elements = []

    def attach(self, element):
        self.elements.append(element)

    def detach(self, element):
        self.elements.remove(element)

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)

# Client code
if __name__ == "__main__":
    element_a = ConcreteElementA()
    element_b = ConcreteElementB()

    visitor = ConcreteVisitor()

    object_structure = ObjectStructure()
    object_structure.attach(element_a)
    object_structure.attach(element_b)

    object_structure.accept(visitor)
