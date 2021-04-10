# Thursday March 25th


# 8-2 create Function Favorite Book & call to it with parameter
def favorite_book(title):
    print(f"One of my favorite books is: '{title.title()}' ")

favorite_book('Alicee in wonderland')

# function that prints multiplication of 2 numbers
def multiply_nums(a, b):
    result = a * b
    print(f"The result of {a}*{b} is: {result}")

multiply_nums(3, 2)


# swap 2 values in their places: a=48 b=78 --> a=78 b=48
def swap(a,b):
    temp = a
    a = b
    b = temp
    print(a, b)

swap(48,78)


print('**********')
# can swap without using temp variable: a, b = b, a
a = 15
b = 3
a, b = b, a
print(a, b)



# Exercises: 8-6, 8-7, 8-8


