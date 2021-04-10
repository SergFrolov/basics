# Chapter 3 LISTS
# Homework: Exercises: 3-1,2,3,4,5,6,7
# pg 40, 46, 47

print('---------------')
# Exercise: 3-1
print("Exercise: 3-1")
names = ['Alex', 'Emin', 'Sergey']
print(names[0])
print(names[1])
print(names[2])


print('---------------')
# Exercise: 3-2
print("Exercise: 3-2")
print(f"Hello {names[0]}, nice meeting you !")
print(f"Hello {names[1]}, nice meeting you !")
print(f"Hello {names[2]}, nice meeting you !")

print('---------------')
# Exercise: 3-3

cars = ['bugatti', 'ferrari', 'tesla', 'bmw']
print("Exercise: 3-3:")
print(f"I would like to own a {cars[0].title()} car.")
print(f"I would like to own a {cars[1].title()} car.")
print(f"I would like to own a {cars[2].title()} car.")
print(f"I would like to own a {cars[3].title()} car.")


print('---------------')
# Exercise: 3-4 (and we continue for homework)
# Guest list
print("Exercise: 3-4")
guests = ['jackson', 'said', 'lenur', 'tyson']
print(f"Hi {guests[0].title()}, I would like to invite you")
print(f"Hi {guests[1].title()}, I would like to invite you")
print(f"Hi {guests[2].title()}, I would like to invite you")
print(f"Hi {guests[3].title()}, I would like to invite you")

print('---------------')
print("Exercise: 3-5")
guests[1] = 'serg'
print(guests)
print(f"Hi {guests[0].title()}, I would like to invite you")
print(f"Hi {guests[1].title()}, I would like to invite you")
print(f"Hi {guests[2].title()}, I would like to invite you")
print(f"Hi {guests[3].title()}, I would like to invite you")

print('---------------')
print("Exercise: 3-6")
guests.insert(0,'lera')
guests.insert(3,'gigi')
guests.append('nick')
print(guests)
print(f"Hi {guests[0].title()}, I would like to invite you")
print(f"Hi {guests[1].title()}, I would like to invite you")
print(f"Hi {guests[2].title()}, I would like to invite you")
print(f"Hi {guests[3].title()}, I would like to invite you")
print(f"Hi {guests[4].title()}, I would like to invite you")
print(f"Hi {guests[5].title()}, I would like to invite you")
print(f"Hi {guests[6].title()}, I would like to invite you")


print('---------------')
print("Exercise: 3-7")

print(f"Sori, {guests.pop().title()}, you're out")
print(f"Sori, {guests.pop().title()}, you're out")
print(f"Sori, {guests.pop().title()}, you're out")
print(f"Sori, {guests.pop().title()}, you're out")
print(f"Sori, {guests.pop().title()}, you're out")

print()
print(guests)
print(f"Hi {guests[0].title()}, you still invited")
print(f"Hi {guests[1].title()}, you still invited")

#del guests[0]
#del guests[1]
# empty the list all together
guests = []
print(guests)
