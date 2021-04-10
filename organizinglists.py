# 03/07/2021
# Organizing lists -- in a sorting way

# 2 different approaches: sort and sorted

# sorted can use it within print
# sort is like a function, you have to execute it separate first
# Same with reverse, you have to run it first: bucket_list.reverse()

# Sorting --> permanent
# Sorted --> temp
cars = ['bmw', 'audi', 'toyota', 'subaru']
sorted_cars_asc = sorted(cars)
sorted_cars_desc = sorted(cars, reverse = True)

# get missing code from Akmals code snippet

sorted_cars_asc2 = sorted(cars)
print(sorted_cars_asc2)
sorted_cars_asc2.reverse()
print(sorted_cars_asc2)


list_size = len(cars)
print(list_size)

#Find length of a string:
print(len('toyota'))




# Exercise 3-8
# Places to visit

bucket_list = ['Hawaii', 'Thailand', 'Japan', 'Everest', 'Bali']

print(sorted(bucket_list))
print(bucket_list)
print(sorted(bucket_list, reverse=True))
print(bucket_list)
bucket_list.reverse()
print(bucket_list)
bucket_list.sort()
print(bucket_list)

# iterable: something that can iterate (loop)
# most data structures, string, not a number
# not boolean

# page 50 is homework
print(len(bucket_list))
