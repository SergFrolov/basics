# from March 21 2021


# Using a flag (temporary holder or counter) (pg 124)
count = 0
for letter in 'hello everyone else':
    if letter == 'l':
        count += 1
print(f"Number of letter 'l' is: {count}")

# homework:
# 1 swap values: a=45, b=78 >> a=78, b=45
# 2 count vowels, from any user input

# Just as a road map for num2
# color = input("Enter your color (green/yellow/red): ")
# color = color.lower().strip()



#Fizz Buzz Programming Question
#That is the case for the FizzBuzz interview question. Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
print("---END---")

# UNDERSTAND the list in dictionary, dictionary in the list
# UNDERSTAND matrix, and multi dimensional arrays
# UNDERSTAND chapter 6




# Homework: print a multiplication table

# Simple Multiplication Table
# scope: form 1 to 10, multiplying by 12

num = 12
for i in range(1,11):
    print(f"{num} * {i}: {num*i}")


# Two dimensional Multiplication Table
n = 10
for row in range(1, n+1):
    for col in range(1, n+1):
        print(row*col, end="\t")
    print()

