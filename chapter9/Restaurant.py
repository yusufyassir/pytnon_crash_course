
class Restaurant:
    """a simple restaurant class"""
    def __init__(self, name, cuisine_type):
        """gives name and cuisine type"""
        self.name = name
        self.cuisine = cuisine_type
    def describe_restaurant(self):
        """a method that prints restaurant info"""
        print(f"the Restaurnant name is {self.name}")
        print(f"and serves a {self.cuisine} type cuisine")
    def open_restaurant(self):
        """print a message to show we are open"""
        print(f"we are open!")
