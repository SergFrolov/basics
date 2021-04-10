# Homework pg 171, 178
# understand page 177
# all exercises from chapter 9 (9-1 to 9-9)


# 9-1 Restaurant exercise
print("# 9-1 Restaurant exercise")
class Restaurant:
    """ This is a restaurant class"""
    #number_served = 0

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"Restaurant name is: {self.restaurant_name}")
        print(f"The kitchen is: {self.cuisine_type}")

    def open_restaurant(self):
        msg = "the restaurant is open"
        print(msg.title())

    def set_number_served(self, number_guests: int):
        self.number_served = number_guests

    def increment_number_served(self):
        self.number_served += 1


# making an actual instance of class
restaurant = Restaurant("Sherdor", "Mid-Asian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2 Three Restaurants: create 3 different instances for the class &
# call describe method for each
print("# 9-2 Three Restaurants")
restaurant1 = Restaurant("La Belle", "Italian")
restaurant2 = Restaurant("El Gallo", "Mexican")
restaurant3 = Restaurant("Chikurin", "Japanese")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


print()
print('----------------')
print("# 9-3 Users: Make a class called User")


class User:

    def __init__(self, first_name, last_name, occupation, address, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.address = address
        self.phone = phone

    def describe_user(self):
        """print summary of user info"""
        print(self.first_name.title())
        print(self.last_name.title())
        print(self.occupation)
        print(self.address)
        print(self.phone)


    def greet_user(self):
        """Print personalized greeting to a user"""
        print(f"Hello {self.first_name.title()}, nice to see you!")


# create several instances, and use both methods for each:
person1 = User("tom", "jefferson", "programmer", "NYC", "212-0000")
person2 = User("george", "jefferson", "programmer", "NYC", "212-0000")
person3 = User("jessica", "thomson", "programmer", "NYC", "212-0000")

person1.describe_user()
person2.describe_user()
person3.describe_user()

person1.greet_user()
person2.greet_user()
person3.greet_user()

print()
print('----------------')


print("# 9-4. Number Served")
new_restaurant = Restaurant("McDonalds", "American")
print(f"people served: {new_restaurant.number_served}")
new_restaurant.set_number_served(30)
print(f"people served: {new_restaurant.number_served}")
new_restaurant.increment_number_served()
print(f"people served: {new_restaurant.number_served}")

print("# 9-5. Login Attempts")
#: Add an attribute called login_attempts to your User class
# pg 171
