# 03/11/2021 - Lists (continue)

cars = ['bugatti', 'ferrari', 'tesla', 'lexus', 'bmw']


# Making numerical List
print("range with start and stop")
for nam in range(1, 4):
    print(nam)


evens = []
print("print all even numbers from 1 to 16 (16 should be included): ")
for num in range(0, 17, 2):
    print(num)
    evens.append(num)
    print(evens)


#numbers raised to 2nd power
print("# List comprehension :")
squares1 = list()
# The list() function creates a list object.
# A list object is a collection which is ordered and changeable.
for num in range(10, 21):
    squares1.append(num**2)
print(squares1)

#same thing, but in a single line
squares2 = [num ** 2 for num in range(10, 21)]
print(squares2)


print("*************** Cars Len")
cars_len = len(cars)
for car in cars:
    print(car)
    print(f"index of the {car} is {cars.index(car)}")

print("looping the list using index ***************")
# for ind in range(len(cars)):
for ind in range(cars_len):
    print(ind)
    print(f"index of the {cars[ind]} is {ind}")

#List comprehension


# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers .
print("******************")
print("exercise [4.4]")

nums = []
for num in range(1, 1000001):
    nums.append(num)
print(f"smallest : {min(nums)}")
print(f"biggest : {max(nums)}")
print(f"total : {sum(nums)}")


# GO thru Chapter 4
# 4.3 exercise