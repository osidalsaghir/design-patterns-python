from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def has(self):
        pass

class Admin(User):
    def has(self):
        return "Has Admin rights"

class SuperAdmin(User):
    def has(self):
        return "Has SuperAdmin rights"

class UserFactory(ABC):
    @abstractmethod
    def create_User(self):
        pass

class AdminFactory(UserFactory):
    def create_User(self):
        return Admin()

class SuperAdminFactory(UserFactory):
    def create_User(self):
        return SuperAdmin()

def get_pet_sound(factory):
    User = factory.create_User()
    return User.has()

if __name__ == "__main__":
    Admin_factory = AdminFactory()
    SuperAdmin_factory = SuperAdminFactory()

    Admin = get_pet_sound(Admin_factory)
    SuperAdmin = get_pet_sound(SuperAdmin_factory)
    
    print(Admin)  
    print(SuperAdmin)