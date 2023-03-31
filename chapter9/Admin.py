class Users:
    def __init__(self, first_name, last_name, number):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.login_attempts = 0

    def describe_user(self):
        print(f"user name is {self.first_name.title()} {self.last_name.title()}")
        print(f"and the phone number is {self.number}.\n")
    def greet_user(self):
        print(f"hello {self.first_name.title()} {self.last_name.title()}")
    def increment_login(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
class Privileges():
    def __init__(self):
        self.privileges = ['can post', 'can ban user', 'can delete post']

    def show_privileges(self):
        for pri in self.privileges:
            print(f" can {pri}")

class Admin(Users):
    """class that defines admins"""
    def __init__(self, first_name, last_name, number):
        super().__init__(first_name, last_name, number)
        self.privilegs = Privileges()

admin_1 = Admin('yusuf', 'yasir', 964804001)

admin_1.privilegs.show_privileges()
