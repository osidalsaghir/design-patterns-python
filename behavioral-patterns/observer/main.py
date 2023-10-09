# Subject (Observable) class
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

# Concrete Subject
class ConcreteSubject(Subject):
    def __init__(self, state):
        super().__init__()
        self._state = state

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state
        self.notify()

# Observer interface
class Observer:
    def update(self):
        pass

# Concrete Observer
class ConcreteObserver(Observer):
    def __init__(self, name, subject):
        self._name = name
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        state = self._subject.get_state()
        print(f"{self._name} received an update. New state: {state}")

# Client code
if __name__ == "__main__":
    subject = ConcreteSubject("Initial State")

    observer1 = ConcreteObserver("Observer 1", subject)
    observer2 = ConcreteObserver("Observer 2", subject)

    subject.set_state("Updated State")
