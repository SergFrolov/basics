# 03/13/2021
# working with part of the list

cars = ['bugatti', 'ferrari', 'tesla', 'lexus']

# slice of the list list_name[start:stop] - start is inclusive, stop is exclusive values
# values: list_name[start], list_name[start+1], ..., list_name[stop-1]

for car in cars[1:3]:
    print(f"the car is: {car}")
# will display positions 1 and 2 ('ferrari' and 'tesla')
print("*************")
for car in cars[:3]:
    print(f"the car is: {car}")
# Same thing as (0-3), positions: 0,1,2


print("*************")

# Semicolumn behind number [2:] means from the end of the list
for car in cars[2:]:
    print(f"the car is: {car}")
# Moving 2 positions from the end, index: 3, 2


print("*************")

#this will display whole list
for car in cars[:]:
    print(f"the car is: {car}")


# If you want to copy
print("---copying---")
cars2 = cars
print(f"cars: {cars}")
print(f"cars2: {cars2}")
cars.append('bmw')
print(f"cars after update: {cars}")
print(f"cars2 after update: {cars2}")



print("*************")
#update 1st element/ (replace the value at 0th index)
cars[0] = 'honda'
print(f"cars after update: {cars}")
