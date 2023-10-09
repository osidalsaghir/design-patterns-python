class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# Singleton class using the metaclass
class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

    def some_business_logic(self):
        pass

# Client code
if __name__ == "__main__":
    # Creating instances of the Singleton class
    singleton1 = Singleton()
    singleton2 = Singleton()

    # Both instances refer to the same object
    print(singleton1 is singleton2)  # Output: True

    # You can access and modify data through either instance
    singleton1.value = "Value set by singleton1"
    print(singleton2.value)  # Output: Value set by singleton1
