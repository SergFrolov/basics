# March 20th 2021
# Nesting: Dictionary in a Dictionary
# Matrix


countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barcelona']
companies = ['level up', 'abc company', 'ola company']
# we have 3 lists, but we can save all values in one list, like below

customers = [companies, cities, countries] # This is lists of lists
print(customers)
print(customers[0])
print(customers[0][0]) # access first list first element

# Print barcelona now:
print(customers[1][2])
print('************')

# Matrix --> multi dimensional array

#multi_dim_nums = [
#    [3, 9, 0]
#    [2, 7, 1]
#    [0, 1, 0]
#]

print()
print('***Nested For-Looping***')
for column in customers:
    print(column)
    for row in column:
        print(row)

print()
print('************')
for city in customers[1]:
    print(city, end='\t')

print()
print('************')
clients = {
    'countries': ['usa', 'russia', 'spain'],
    'cities': ['new york', 'moscow', 'barcelona'],
    'companies': ['level up', 'abc company', 'ola company']
}

# print(clients)
print(clients['cities'])
# print moscow
print(clients['cities'][1])

print()
print('************')
users = {
    'user_0': {'name': 'john', 'age': 25, 'city': 'brooklyn'},
    'user_1': {'name': 'jane', 'age': 20, 'city': 'paris'},
    'user_2': {'name': 'serg', 'age': 35, 'city': 'tokyo'}
}

print(users['user_2']['name'])
print('************')
# using items() to access both: key and value
for username, details in users.items():
    print(f"{username}: {details['name']}")


print('************')
# Example of end parameter for print function
# basically using this parameter you can put anything at end of the current print line
# it is useful when recursively printing elements
print("Hello", end = '@')
print("gmail.com")

print("Welcome to", end=' ')
print("NYC")