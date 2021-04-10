# all exercises from chapter 10 --> files
from datetime import date #need for exercise 10-4

# 10-1. Learning Python
filepath = '/Users/Serja_boi/dev/basics/files_exceptions/learning_python.txt'
print()
print("10-1. Learning Python")
print("Task1: Read in the entire file")

with open(filepath) as file:
    lines = file.read()
    print(lines)

file.close()

print()
print("Task2: Looping thru file object (for loop)")

#always need to do this way
with open(filepath) as py_language:
    for line in py_language:
        print(line, end='') # prints this individual line as reads (line by line)
py_language.close()


print()
print()
print("Task3: store lines in list, then work them outside of 'with open' block")
lines = []
with open(filepath) as text:
    line = text.read()
    lines.append(line)

print(lines)
print()
print("***While Loop***")

l = 0
while l < len(lines):
    print(lines[l])
    l += 1

print()
print("***For Loop***")

for linee in lines:
    print(linee)

print()

text.close()


# 10-2. Learning C
print("10-2. Learning C")
with open(filepath) as a:
    line = a.read()
    print(line.replace('Python', 'java'))

a.close()

# 10-3. Guest
print("10-3. Guest")

name = input("Hello, your name please: ")
filepath = '/Users/Serja_boi/dev/basics/files_exceptions/guest.txt'
with open(filepath, 'w') as guests:
    guests.write(name)  #this would have overwritten the whole file if it wasnt empty

guests.close()
print()


#10-4. Guest Book
print("10-4. Guest Book")

filepath = '/Users/Serja_boi/dev/basics/files_exceptions/guest_book.txt'
entry = ''
while entry != 'q': # press q to exit
    entry = input("Hello, enter your name please: ")
    if entry != 'q':
        print(f"Hello nice to see you {entry.title()} !!")
        with open(filepath, 'a') as visitors:
            visitors.write(f"{entry.title()} visited on {date.today()}\n")

visitors.close()
print()