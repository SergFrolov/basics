# 03/18/2021
# Data Struct: Dictionaries

# - Dictionaries are used to store data values in key:value pairs.
# - A dictionary is a collection which is ordered*, changeable and does not allow duplicates
# - Dictionaries are used with curly braces

#   - KEY is unique, value is not unique
#   Can have only 1 first_name KEY and can have 2+ values repeating for diff keys.
#   friend = {'first_name': 'Vitali', 'last_name': 'Vitali'}

# In js: hashtable, hashmap

#Example of dictionary:
#alien.py (pg 96)
alien_0 = {'color': 'green', 'points': 5}
# data stored in key:value pairs
print(alien_0['color'])
print(alien_0['points'])

my_house = dict() #declare dictionary data struct
my_car = {"brand": "Ford", "model": "Mustang", "year": 1964, 1: 'value of 1'}

print(my_car)
print(my_car['brand'])
print(f"the value of key 'brand' is: {my_car['brand']}.")
print(my_car[1]) # this is not index, my_car has key=1

my_car['price'] = 125000.00
print(my_car)

# updating the value in dictionary:
print("price was updated --------------")
my_car['price'] = 120000.00
print(my_car)


# removing the values from dictionary
print("element with key 1 is being removed --------------")
del my_car[1]
print(my_car)


# match with Akmals code snippet from Thursday March 18th
