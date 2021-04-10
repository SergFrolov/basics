# 04/04/2021
# try except in python
# try catch in Java

# When you have expected errors coming
# use try and handle error if it comes with except

# Exception handling


filepath = "/Users/Serja_boi/dev/basics/advanced1/students.txt"
# /advanced1 before students

try:
    print('trying block has started ...')
    with open(filepath, 'a') as people:
        #   a is for append. it appends the given value
        print("writing to a file")
        people.write("\nSergey")  # write with a  new line character

    with open(filepath, 'r') as students:
        lines = students.readlines()
        print(lines)

except FileNotFoundError as err:
    print(err)
    print("Enter correct file path. Check your file path.")

print("***")


# will be a lot of try/ except with selenium
try:
    print(5/0)
except ZeroDivisionError:
    print("Cant divide by zero")
else:
    print("this is else block")
    # else will be executed if try is successful

finally:
    # Finally is something you Always want to do regardless of try except
    print("I am a 'finally' block, Im always executed")
    print("*************")


print("Program has completed!")



# HW (from akmals text file):

# (done) have github ready and running
# All exercises in Chapter 10
# read about version control systems (git)
# read about exception handling
