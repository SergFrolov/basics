# 04/04/2021
# how to Write to a file

# -w will fully overwrite the file (erase all previous things)
# --> truncate and add new stuff
# -a will append, write to the end of file (get to keep previous things)
# mode = 'r' or just give as second parameter 'r'. Ofc no writing is allowed

# this is how log file is created

filepath = "/Users/Serja_boi/dev/basics/advanced1/students.txt"
# using absolute path here, bc can access from anywhere

# example of appending to a file
with open(filepath, 'a') as people:
    #   a is for append. it appends the given value
    print("writing to a file")
    people.write("\nSergey") # write with a  new line character

with open(filepath, 'r') as students:
    lines = students.readlines()
    print(lines)

students.close()
print("Program is completed")
