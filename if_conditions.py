# if statements

#if expression:
#    code here when expression is True
#else:
#    code here when expression is False

num1 = 20
num2 = 3

if num1 < num2:
    print("expression is true")
    print("you can do something here")
else:
    print("expression is false")

print("If statement completed here")


print("***TRYING with Range***")

num = 0
if num not in range(5):
    print("expression is true, num is within range")
else:
    print("expression is false")

print("******")
if num != 0:
#if num == 0:
    print("true")
else:
    print("false")



print("checking string type input")
name = input('Please enter your name: ')
if name.strip().lower() == 'john doe':
    print(f"We have missed you: {name}")
else:
    print("Name is incorrect!")


print("exercise --------- ")
nums = [45, 4, 5, 6, 3, 10]
#find and print 5 if it is in the list

for num in nums:
    if num == 5:
        print(num, 'completed')
        break #(to break out of for loop)
    else:
        print(num, "is not 5")


# For homework, find how many 5s we have in the list:
# nums = [45, 4, 5, 6, 3, 5, 10, 666, 123, 5]
# GO THRU CHAPTER 5

