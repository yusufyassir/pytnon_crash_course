class Users:
    def __init__(self, first_name, last_name, number):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number

    def describe_user(self):
        print(f"user name is {self.first_name.title()} {self.last_name.title()}")
        print(f"and the phone number is {self.number}.\n")
    def greet_user(self):
        print(f"hello {self.first_name.title()} {self.last_name.title()}")

user_1 = Users('yusuf', 'yassir', 964804001)

user_1.describe_user()
user_1.greet_user()