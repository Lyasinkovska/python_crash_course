class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Welcome to "+self.restaurant_name + " restaurant of " + self.cuisine_type + " food.")

    def open_restaurant(self):
        print(self.restaurant_name + " is open now.")

my_restaurant = Restaurant("Kitchen", "ukrainian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

