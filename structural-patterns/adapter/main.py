# Target interface
class Target:
    def rights(self):
        pass

# Adaptee (the class to be adapted)
class Adaptee:
    def specific_rights(self):
        return "a" #this a means admin role in database 

# Adapter (using class composition)
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def rights(self):
        if self.adaptee.specific_rights() == "a":
            return "Has Admin rights"

# Client code
if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    result = adapter.rights()
    print(result)  # Output: a translated to Admin rights'
