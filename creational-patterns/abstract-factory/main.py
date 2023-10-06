class UserFactory:
    def __init__(self, email, name):
        self.email = email
        self.name = name
        
    def create_user(self):
        pass

    def create_permission(self):
        pass
    
    def getUserDetais(self):
        user = self.create_user();
        return '\n user id: ' + str(user.get_id()) +', User email: ' + user.get_email() + ', Permission: ' + self.create_permission() + '\n'

class AdminUser(UserFactory):
    def create_user(self):
        return Admin(self.email, self.name)

    def create_permission(self):
        return "Admin permission (read))"

class SuperAdminUser(UserFactory):
    def create_user(self):
        return SuperAdmin(self.email, self.name)

    def create_permission(self):
        return "Super Admin permission (read, write, update, delete))"

class User:
    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.id = id(self)

    def get_email(self):
        pass
    def get_id(self):
        return self.id

class Admin(User):
    def get_email(self):
        return  f"admin_{self.email}"

class SuperAdmin(User):
    def get_email(self):
        return  f"super_admin_{self.email}"

def createdUser(factory):
    user = factory.create_user().get_email()
    permission = factory.create_permission()
    return f"{user} - {permission}"

if __name__ == "__main__":
    admin = AdminUser('osid.alsagheer@gmail.com', 'Osid Alsagheer')
    super_admin = SuperAdminUser('test@gmail.com', 'test test')

    print(admin.getUserDetais())
    print(super_admin.getUserDetais())
