# 04/04/2021
# how to read files
# YAML files

filepath = "/Users/Serja_boi/dev/basics/advanced1/students.txt"
# i used absolute path here, bc can access from anywhere

# need so save the opened object to variable (with alied name)
# then read the file through looping
with open(filepath) as students:
    content = students.read() # using read function to get the contents from file
    print(content)


# always close file in the end, so theres no interference
students.close()


print("------")
with open(filepath) as students:
    for line in students: # read line by line
        print(line, end='')

students.close()


# Making a list of lines from file
print("------")
with open(filepath) as students:
    lines = students.readlines()

    print(lines)

# Now loop that list:
for line in lines:
    print(line.strip()) # will print each element

# we use .strip() if theres empty spaces (or new lines)

students.close()
