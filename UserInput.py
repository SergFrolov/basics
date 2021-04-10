
print("***************")
#Example of input from the user
num3 = int(input("enter the num3: "))
num4 = 7

if num3 == num4:
    print("expression is true")
else:
    print("expression is false")

#print("If statement completed here")


print("***************")
#msg = True #Binary is upper case in python

# if you enter: msg = 0 its False, anything 1 and beyond is True

msg = bool(input("enter status (True/False): "))

if msg: #this means true automatic
    print("expression is true")
else:
    print("expression is false")

# **DOUBLE CHECK THIS ONE



msg = input("enter the number: ")
if msg.strip() != '':
    print(f"this message was entere: \n'{msg}' ")
else:
    print("whitespace was entered")

#  '\n' means new line