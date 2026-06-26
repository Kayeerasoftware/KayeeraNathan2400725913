class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)
        print()


restaurant1 = Restaurant("Chicken Tonight, Nakulabye", "Fast Food")
restaurant2 = Restaurant("Cafe Javas", "Continental")
restaurant3 = Restaurant("Pizza Hut", "Italian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()