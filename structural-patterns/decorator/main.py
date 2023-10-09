# Component interface (the common interface for all components)
class Coffee:
    def cost(self):
        pass

# Concrete component (the basic coffee)
class SimpleCoffee(Coffee):
    def cost(self):
        return 5  # Base cost of a simple coffee

# Decorator (abstract decorator class)
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete decorators (additions to the coffee)
class Milk(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2  # Additional cost of milk

class Sugar(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1  # Additional cost of sugar

# Client code
if __name__ == "__main__":
    simple_coffee = SimpleCoffee()
    print(f"Cost of Simple Coffee: ${simple_coffee.cost()}")

    milk_coffee = Milk(simple_coffee)
    print(f"Cost of Coffee with Milk: ${milk_coffee.cost()}")

    sugar_coffee = Sugar(simple_coffee)
    print(f"Cost of Coffee with Sugar: ${sugar_coffee.cost()}")

    milk_and_sugar_coffee = Milk(sugar_coffee)
    print(f"Cost of Coffee with Milk and Sugar: ${milk_and_sugar_coffee.cost()}")
