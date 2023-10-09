import copy

class UserPrototype:
    def clone(self):
        return copy.deepcopy(self)

class Admin(UserPrototype):
    def __init__(self, name):
        self.name = name

    def rights(self):
        return f"{self.name}, has Admin rights"

if __name__ == "__main__":
    original_admin = Admin("User as admin")
    cloned_admin = original_admin.clone()

    print(original_admin.rights())  
    print(cloned_admin.rights())    

    print(original_admin is cloned_admin)  # Output: False
