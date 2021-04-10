# March 20th 2021

# Dictionaries and lists are mutable (changeable)
# Tuples are data structs that are not changeable

my_car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Ways for access the Dictionary
for key in my_car:
    print("---------------------")
    print({key})
    print({my_car[key]})

# use of items
print("*****************")
# sorted is temp, sort is permanent
for name in sorted(my_car.keys()):
    print(f"{name} somebody's favorite car")

print("*****************")
print("Now values")
# go thru values
for val in my_car.values():
    print(f"{val} somebody's favorite car")



print("*****************")
# Nesting values
# 6-5 Rivers pg 108
rivers = {'nile': 'egypt', 'tigers': 'iraq', 'amazon': 'brazil', 'mississippi': 'usa'}

# With items, you can access both elements: key and value
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Homework do 6-6 Polling, page 108

