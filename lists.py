#   Lists (Arrays)
#   Operations:
#   create, access, add element, remove elements
#   copy

# list example + delete + pop
mylist = ['hello', 'there']
print(mylist)
print(mylist[0])

print('---------------')

motorcycles = []
motorcycles.append('suzuki')
print(motorcycles)
print(motorcycles[0])

num = 11
odds = [1, 3, 5, 7, 9]
# indexes start with 0
# we have 5 elements in a list
# number of elements is the SIZE
# 5 is the size here
# to access the last element is: "list_name-1"

friends = ['jackson', 'said', 'lenur', 'tyson']
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

print('---------------')

# Access
print(f"friends: {friends}")
print(f"friend[0]: {friends[0]}")
print(f"friend[1]: {friends[1]}")
print(f"friend[2]: {friends[2]}")
print(f"friend[3]: {friends[3]}")

print('---------------')
# negative index, meaning strting from back of the list (from right side)
print(f"friend[-1]: {friends[-1]}")
print(f"friend[-1]: {friends[-1].title()}")

print('---------------')
# These two are the same thing
print(f"friend[-1]: {friends[-1]}")
print(f"friend[3]: {friends[3]}")
# When you move from the back of the list
# YOu find index by subtracting from SIZE
# Which is the number of elements


# list.append(new_element) - this adds element to end of list
# list.insert(index, new_element) - this adds element to given index, shifts all elements to right
friends.append('obama')
print(f"new friends list: {friends}")

friends.insert(0, 'mess9')
friends.insert(0, 'ronaldo')
print(f"new friends list: {friends}")

# most of the time will use append
# SHIFT + Command + Up/Down key:
# to move the current line up and down

print('---------------')
# reset (change) element in certain position
# Equal sign means we 'Assign' the value
friends[2] = 'mark'
print(f"new friends list: {friends}")

# We replaced Jackson, but also we lost that value



print('---------------')
# to remove element
#friends.remove
friends.remove('mark')
print(f"new friends list, after removing mark: {friends}")


print('---------------')
# friends.pop(4) --> pop() function informs us what its removing
removed_friends = []
removed_friends.append(friends.pop(4))
print(f"new friends list after popping index4: {friends}")
print(removed_friends)

# Easy way to pop and append to different list at the same time
# removed_friends = []
# removed_friends.append(friends.pop(4))


# to remove full list, just reassign an empty list to it
# friends =[]
