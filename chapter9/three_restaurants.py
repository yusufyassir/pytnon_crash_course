class Restaurant:
    """a simple restaurant class"""
    def __init__(self, name, cuisine_type):
        """gives name and cuisine type"""
        self.name = name
        self.cuisine = cuisine_type
    def describe_restaurant(self):
        """a method that prints restaurant info"""
        print(f"the Restaurnant name is {self.name.title()}")
        print(f"and serves a {self.cuisine.title()} type cuisine. \n")
    def open_restaurant(self):
        """print a message to show we are open"""
        print(f"we are open!")

rest_1 = Restaurant('kfc', 'chicken')
rest_2 = Restaurant('pizza hut', 'pizza')
rest_3 = Restaurant('alqds', 'traditional')

rest_1.describe_restaurant()
rest_2.describe_restaurant()
rest_3.describe_restaurant()