# State interface
class State:
    def handle(self):
        pass

# Concrete State classes
class StateA(State):
    def handle(self):
        return "State A is handling the request."

class StateB(State):
    def handle(self):
        return "State B is handling the request."

# Context class
class Context:
    def __init__(self):
        self._state = StateA()  # Initial state

    def set_state(self, state):
        self._state = state

    def request(self):
        return self._state.handle()

# Client code
if __name__ == "__main__":
    context = Context()

    # Initial state
    result1 = context.request()
    print(result1)  # Output: "State A is handling the request."

    # Change state to StateB
    context.set_state(StateB())
    result2 = context.request()
    print(result2)  # Output: "State B is handling the request."
