class Restaurant:
    """a simple restaurant class"""
    def __init__(self, name, cuisine_type):
        """gives name and cuisine type"""
        self.name = name
        self.cuisine = cuisine_type
        self.numbers_served = 78
    def describe_restaurant(self):
        """a method that prints restaurant info"""
        print(f"the Restaurnant name is {self.name}")
        print(f"and serves a {self.cuisine} type cuisine")
    def open_restaurant(self):
        """print a message to show we are open"""
        print(f"we are open!")
    def set_number_served(self, customers):
        """set number of served customers"""
        self.numbers_served = customers
    def increment_number_served(self, customers):
        """increments each time customers are served"""
        self.numbers_served += customers

rest_1 = Restaurant('pizza hut', 'pizza')
print(f"{rest_1.numbers_served} cutomers have been served")
#change number of served customers
rest_1.set_number_served(50)
print(f"{rest_1.numbers_served} cutomers have been served")
rest_1.increment_number_served(30)
print(f"{rest_1.numbers_served} cutomers have been served")