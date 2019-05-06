
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Welcome to "+self.restaurant_name + " restaurant of " + self.cuisine_type + " food.")

    def open_restaurant(self):
        print(self.restaurant_name + " is open now.")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name = '', cuisine_type = ''):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self. flavors = ["banana", "chocolate", "vanilla"]

    def ice_flavors(self):
        print(self.flavors)



my_icecream = IceCreamStand("Frozen")
my_icecream.describe_restaurant()
my_icecream.ice_flavors()
