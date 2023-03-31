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

user_1 = Users('yusuf', 'yasir', 964804001)
user_1.increment_login()
user_1.increment_login()
user_1.increment_login()
user_1.increment_login()
user_1.increment_login()
print(f"you have attempted to login {user_1.login_attempts} times")
user_1.reset_login_attempts()
print(user_1.login_attempts)
