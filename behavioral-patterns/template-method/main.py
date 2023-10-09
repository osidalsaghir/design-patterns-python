# Abstract class defining the template method
class AbstractClass:
    def template_method(self):
        self.common_step()
        self.specialized_step()

    def common_step(self):
        print("This is a common step shared by all subclasses.")

    def specialized_step(self):
        pass

# Concrete subclass 1
class ConcreteClass1(AbstractClass):
    def specialized_step(self):
        print("Specialized step for ConcreteClass1")

# Concrete subclass 2
class ConcreteClass2(AbstractClass):
    def specialized_step(self):
        print("Specialized step for ConcreteClass2")

# Client code
if __name__ == "__main__":
    concrete1 = ConcreteClass1()
    concrete1.template_method()

    concrete2 = ConcreteClass2()
    concrete2.template_method()
