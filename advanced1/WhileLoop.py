# 3/21/2021 Sunday

# temporary allocated memory:
# Read up: stack, buffer (done)

# WHile looping

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number+=1
print("------------------")
current_number = 5
while current_number >= 1:
    print(current_number)
    current_number-=1

print()
print("***Game***")
# enter colors get points, green: 15, yellow: 10, red: 5
# other colors or something you loose
# q or quit to end the game

color = None
while color != 'quit' or color != 'q':
    color = input("Enter your color (green/yellow/red): ")
    color = color.lower().strip()
    points = 0
    if color == 'quit' or color == 'q':
        break
    elif color == 'green':
        points = 15
    elif color == 'yellow':
        points = 10
    elif color == 'red':
        points = 5
    else:
        print("Sorry, that's not right color, You lost!")
    print(f"You earned {points} points!")
print("closing the game...")
