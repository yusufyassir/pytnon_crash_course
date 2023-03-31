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

class ice_cream_stand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavours = ['vanila', 'chocolate', 'mint']

    def available_flavours(self):
        for flavour in self.flavours:
            print(f"{flavour.title()} is available")

rest_1 = ice_cream_stand('dream', 'icecream')

rest_1.available_flavours()