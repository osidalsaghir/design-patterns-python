class Flyweight:
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        pass

class ConcreteFlyweight(Flyweight):
    def operation(self, unique_state):
        shared = self._shared_state
        return f"ConcreteFlyweight: ({shared}) and ({unique_state})"

class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self._flyweights:
            self._flyweights[shared_state] = ConcreteFlyweight(shared_state)
        return self._flyweights[shared_state]

    def list_flyweights(self):
        return list(self._flyweights.keys())

def main():
    factory = FlyweightFactory()

    fw1 = factory.get_flyweight("SharedState1")
    print(fw1.operation("UniqueState1"))

    fw2 = factory.get_flyweight("SharedState2")
    print(fw2.operation("UniqueState2"))

    fw3 = factory.get_flyweight("SharedState1")
    print(fw3.operation("UniqueState3"))

    print("Flyweights in the factory:", factory.list_flyweights())

if __name__ == "__main__":
    main()
