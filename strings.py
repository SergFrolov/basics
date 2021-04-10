# March 4th 2021    Strings

#String (str)

fullname = "john doe"
msg = "we are looking at string functions in python."
print(fullname)

#We can use several functions, using a dot:

print(fullname.upper())
print(fullname.title())
print(msg.replace('.', '!!!'))
print(msg.replace('python', 'java').title())


#Concatenation

msg1 = fullname + ", " + msg

print(msg1)
print(fullname.title() + ", " + msg)


# working with Whitespace in string: \t, \n, etc

print(fullname.title() + "\t, " + msg )
print(fullname.title() + ",\n\t\t\t " + msg )
#remove whitespaces
msg2 = fullname.upper() + "\n\t\t\t" + msg
print(msg2)
print(msg2.replace('\t', '')) #we removed all tabs (using replace)
#strip command (only used for String data type)
msg3 = '\n\t\t\t' + fullname.upper() + ", " + msg
print(msg3)
print(msg3.strip()) #str.strip() - removes leading and preceding whitespaces


#fstring
# it is more easy to do Concatenation, dont have to use +
# making it easier syntax
msg4 = f"{fullname.upper()}, {msg}"
print(msg4.replace('.', '!!!'))

msg5 = f"{fullname.upper()}, {msg} \t ashqhqhq;hrhththeehehewnwqqqqkkkrrjj"
print(msg5)

#When will use single quotations, make sure to wrap a string into double quotes
message = "One of Python's strengths is its' diverse community"
print(message)

#numbers and fstring
num = 456
num2 = 600

print(num+num2)
print(f"num + num2 = {num+num2}")
print(f"num / num2 = {num/num2}")

# str(expression) - this will convert data type to string
print("Value of num is: " + str(num))
# so instead we use fstring, more efficient

num3 = "753" #its a string data type
print(f"num + num3 = {num + int(num3)}")
# using int(num3) we convert to the integer data type

#exponent is two stars: 3 ** 2
print(3 ** 2)
print(f"3^2 = {3**2}") #Again, this is why fstring is useful

#there are also float numbers (with decimals)
# and also you can round the numbers


#This functions return Boolean values, and we concatenate with fstring
print(f"fullname.isdigit() >> {fullname.isdigit()}")
print(f"fullname.isdigit() >> {fullname.islower()}")


#fstring converts everything to string

