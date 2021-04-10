# 03/18/2021

# Walk over through whole material
# add something in the beginning of the list
# Use list_name.insert statement

new_users = ['mary', 'akmal', 'said', 'jennifer']
print(new_users)
new_users.insert(0, 'serg')
print(new_users)

#if you need to see what you are removing from list, use: pop
deleted_elem = new_users.pop()
print(deleted_elem)
print(f"The updated list: {new_users}")

# You can look element-by-element in a list using for loop:
for person in new_users:
    print(person)

# check if you have a specific person in the list:
# check if mary is in the list
# use for loop and if statement to solve
for person in new_users:
    if person == 'mary':
        print(f"Heyy {person.title()}")
        break
#Alternative:
#if 'mary' in new_users:
#    print(f"Heyyy {person.title()}")
