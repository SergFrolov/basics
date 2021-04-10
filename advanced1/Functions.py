# 3/21/2021 Sunday Part 2

# FUNCTIONS
# Chapter 8 Functions
# Modules = when you store your function in a separate file
# You store functions in separate files called modules to help organize your main program files.

# declare and define (a function)
def greet_user():
    """this is docstring, it's something that describes a function"""
    print("Hello!")
# If you want to make a call to a function/ Execution:
# greet_user()


def greet_user_by_name(name):
    """It will say hello and use the name entered (parameter)"""
    print(f"Hello, {name.title()}")


def sum_of_numbers(num1, num2, num3):
    print(f"The sum of {num1}, {num2}, {num3} is: {num1+num2+num3}")


def describe_pet(pet, pet_name):
    print(f"I have a {pet} and we call it {pet_name.title()}")


# optional parameter (will be used by deafult if not provided)
def sum_the_seven(num1, num2=7):
    print(f"the sum_the_seven sum is: {num1+num2}")


greet_user()
greet_user_by_name("Serg")  # Here we pass name as a function parameter
sum_of_numbers(2, 4, 6)
describe_pet("cat", "fluffy")
sum_the_seven(5)

# Some string manipulation
sentence = 'Hello There!'
print(f"The length of the string is: {len(sentence)}")


s = 'Hello'
match = False
if s[:3] + s[3:] == s:
    # Here, we take characters positioned [0,1,2] and concatenate them with characters positioned at [3, onward to end of string]. And therefore its the same thing as the original word= 'Hel'+'lo'
    match = True
    print(match)
else:
    print(match)




# *** LeetCode twoSum problem ***


# enumarate nums [(0,1),(1,3),(2,11),(3,2),(4,7)]

def two_sum(nums, target):

    aux_dic ={}
    for i, num in enumerate(nums):
         result = target - num
         if num not in aux_dic:
            aux_dic[result] = i
         else:
             return [aux_dic[num], i]


nums = [1,3,11,2,7]
target = 9

x = two_sum(nums, target)
print(x)


#nums = [5, 3, 3]
#target = 8
