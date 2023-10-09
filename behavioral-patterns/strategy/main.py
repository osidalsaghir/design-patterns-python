# Strategy interface
class PaymentStrategy:
    def pay(self, amount):
        pass

# Concrete Strategy classes
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, name):
        self.card_number = card_number
        self.name = name

    def pay(self, amount):
        print(f"Paid ${amount} with credit card ending in {self.card_number} (Cardholder: {self.name})")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid ${amount} via PayPal (Email: {self.email})")

# Context class
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)

    def checkout(self):
        total_amount = sum(item['price'] for item in self.cart)
        self.payment_strategy.pay(total_amount)

# Client code
if __name__ == "__main__":
    # Create concrete strategy instances
    credit_card = CreditCardPayment("1234-5678-9876-5432", "John Doe")
    paypal = PayPalPayment("john.doe@example.com")

    # Create a shopping cart and set the payment strategy
    cart1 = ShoppingCart(credit_card)
    cart2 = ShoppingCart(paypal)

    # Add items to the shopping carts
    cart1.add_item({"product": "Product 1", "price": 50})
    cart1.add_item({"product": "Product 2", "price": 30})

    cart2.add_item({"product": "Product 3", "price": 70})
    cart2.add_item({"product": "Product 4", "price": 20})

    # Checkout using different payment strategies
    cart1.checkout()  # Uses CreditCardPayment
    cart2.checkout()  # Uses PayPalPayment
