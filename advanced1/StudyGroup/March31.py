# Wednesday March 31 Study Group

# DataStructures: tuples, lists, dictionaries: matrix (list in list)
# functions
# Classes and Objects

# Data Structures
# Tuples --> immutable (not modifiable)
# regular parenthesis
cars_t = ('toyota', 45, 'bmw')
print(cars_t)
print(f"the car is: {cars_t[0]}")
# Assignment or Deletion is illegal for tuples
# for example, that illegal: cars_t[2] = 'honda'

# to access tuple element by element:
for car in cars_t:
    #print(car)
    print(f"Index of the {car} is: {cars_t.index(car)}")

# if want to see index: {cars_t.index(car)}


print("******")
print(" LISTS ")
# Lists (array) --> mutable (changeable)
# square brackets
# collection of items in a particular order
# this how we can create list: cars_l = []

cars_l = ['toyota', 45, 'bmw']
print(cars_l)
# access the list elem by elem (use for loop)
for car in cars_l:
    print(car)

# Manipulation on the lists: assign, insert, append,  remove, del, pop

# Assignment
cars_l[2] = 'honda'
print(cars_l)
# insert, adds element on that index, and shifts others to the right
cars_l.insert(1, 'mercedes')
print(cars_l)
# append (add at the end of list)
cars_l.append('tesla')
cars_l.append('tesla')
cars_l.append('hyundai')
print(cars_l)


print("look here, take out duplicates")
# Ask Akmal how to remove all duplicates from the list
# Remove --> only removes one value (no duplicates!)
# to only remove one value: cars_l.remove('tesla')
# while loop to delete all duplicates
while 'tesla' in cars_l:
    cars_l.remove('tesla')
print(cars_l)

# delete
# if do range del cars_l[1:4]
# but 4 is not inclusive (+1 to the index you want removed)
del cars_l[1]
print(cars_l)

# pop,
# because you can assign to the variable and
print(f"I just removed: {cars_l.pop(2)}")

print(cars_l) #just to see value at position 2 actually was removed

# to fully delete list (remove whole list)
# cars_l = [] is same as: cars_l.clear()
#del cars_l
cars_l = []
print(cars_l)

cars_l.append('kia')

if not cars_l:
    print("List is empty")
elif cars_l:
    print("not empty")


print("******")
print(" DICTIONARIES ")

# DICTIONARY: key:value pairs
# key must be unique, value can repeat
# curly braces {} represent dictionary

# dictionary_name = {"key": "value", "key2": "value2"}
teacher = {
    "first_name": "Akmal",
    "last_name": "Husanov",
    "age": 30,
    "occupation": "banker",
    "years_on_job": 5,
    "business": "level up"
    }


# to print the whole dictionary:
# print(teacher)

# Goal is to describe your teacher
print(f'The name of teacher is: {teacher["first_name"]} {teacher["last_name"]}')
print(f'He is {teacher["age"]} years old and he is a {teacher["occupation"]}')
print(f'His experience in the job is {teacher["years_on_job"]} years')

# Manipulation:
# Same as list, add append remove
# keep thinking in terms of key-value

# Replace occupation title to manager:
teacher["occupation"] = "manager"
print(f'He is {teacher["age"]} years old and he is a {teacher["occupation"]}')
print(teacher)

# Totally new pair (key-value)
teacher["driver_license"] = True
if teacher["driver_license"] == True:
    print(f'{teacher["first_name"]} knows how to drive!')
else:
    print(False)

# see if the key 'driver_license' is in the dictionary teacher
if "driver_license" in teacher:
    print("YESSSS")
if 'Akmal' in teacher.values():
    print("YESSSS2")
# also check items --> keys and values (both)

rivers = {
    'nile':'egypt',
    'tigers':'iraq',
    'amazon':'brazil',
    'mississppi':'usa'
    }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")
# river is key, country is value
# .items() is for both: key and value at same time


# Example of simple function
def avg_of_two(num1, num2):
    avg = (num1 + num2)/2
    return avg

print(f"the avg is: {avg_of_two(3, 6)}")