class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print("Welcome to "+self.restaurant_name + " restaurant of " + self.cuisine_type + " food.")

    def open_restaurant(self):
        print(self.restaurant_name + " is open now.")
        #print(self.number_served)

    def set_number_served(self, people):
        self.number_served = people
        print(self.number_served)

    def increment_number_served(self, inc_people):
        self.number_served += inc_people
        print(self.number_served)




my_restaurant = Restaurant("Kitchen", "ukrainian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.number_served = 80
my_restaurant.set_number_served(7)
my_restaurant.increment_number_served(9)





