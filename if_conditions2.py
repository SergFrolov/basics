# 03/ 14/ 2021 if statement (continue)

# AND / OR expressions
num = 2
if num >= 1:
    print(f"number is equal or greater than 1")
else:
    print(f"number is less than 1.")

age = 3
if 0 <= age <=4:
    print("Your admission cost is $0.")
elif 4 < age < 18:
    print("Your admission cost is $5.")
elif 18 <= age < 140:
    print("Your admission cost is $10.")
else:
    print("Invalid age was entered, bye!")

#flow of execution is important
#age = int(input('enter the visitors age: '))
age = 4
price = 0
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 140:
    price = 10
else:
    print("invalid")
print(f"your admission cost is ${price}.")

print("5-3. Alien Colors #1 ********")
#alien_color = input('enter the alien color (green/yellow/red): ')
alien_color = 'green'
if alien_color == 'green':
    print(f"You just earned 5 points!!")
elif alien_color == 'yellow':
    print(f"You just earned 2 points, whee!")
elif alien_color == 'red':
    print(f"You just earned 10 points, you killen it!")
else:
    print(f"no points, sorry")




# EXERCISE
#1

number = int(input("Enter an integer: "))
if number % 3 == 0 and number % 5 == 0:
    print("FuzzBuzz")
elif number % 3 == 0:
    print("Fuzz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("Not divisible by 3, 5")

# DO homework exercises, the Akmal included in the snippet
