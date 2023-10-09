# Complex subsystem classes
class SubsystemA:
    def operation_a(self):
        return "Subsystem A: Operation A"

class SubsystemB:
    def operation_b(self):
        return "Subsystem B: Operation B"

class SubsystemC:
    def operation_c(self):
        return "Subsystem C: Operation C"

# Facade class
class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()
        self.subsystem_c = SubsystemC()

    def operate(self):
        result = []
        result.append(self.subsystem_a.operation_a())
        result.append(self.subsystem_b.operation_b())
        result.append(self.subsystem_c.operation_c())
        return "\n".join(result)

# Client code
if __name__ == "__main__":
    facade = Facade()
    result = facade.operate()
    print(result)
