# Foundation of Iterations
# Loops
# Flow control


# Syntax in python language (FOR loop):
#for temp_var in iterable:
    #some code to execute

# array = list
# initial example:
friends = ['jackson', 'said', 'lenur', 'tyson']
# the size of friends = num of elements: 4
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

print('************')
# Now using for loop, it takes only 2 lines

for friend in friends:
    print(friend.title())




h_list = ['hello', 'hi', 'hey']
for h in h_list:
    print(h)



numbers = [3,5,7]

# print line by line
for number in numbers:
    print(number)


#to remove list in right way, just assign empty list to your list
numbers = []
print(numbers)


# remove and delete: remove 'honda' have to use actual value
# delete you have to use index
# pop if you want to see what you removed, used with print()


# Sorted is temporary and Sort is permanent
# Can use Sorted with print
# and Sort have to use as a command (separately)
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)


#chapter 4 is on thursday

#Just practice loops