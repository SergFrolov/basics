# 03/25/2021 Functions with return statements


def get_formatted_name(firstname: str, lastname: str):
    name = f"{firstname.title()} {lastname.title()}"
    return name


# getter, setter functions
def get_desc_of_what_you_want_to_get():
    #logic
    return


def set_desc_of_what_you_want_to_update():
    pass


# generate sequence of numbers
def get_list_of_even_numbers(num):
    # create empty list:
    #   nums = []
    #   nums = list()

    nums = list(range(2, num+1, 2))
    # or
    # nums = [range(2, num+1, 2)]

    return nums


def get_list_of_odd_numbers(nums):
    odd_nums = list(range(1, nums+1, 2))
    return odd_nums


# FInd the most used letter in a phrase
def get_letter_counts(text: str) -> dict:

    letter_count = {}
    most_frequent = {}

    for letter in text:
        letter_count[letter] = letter_count.setdefault(letter, 0)+1

    #most_frequent = max(letter_count.values())

    return letter_count

print(get_letter_counts("aabbaba"))


def print_username(users: list):
    #we are explicitly saying the parameter will be List
    for user in users:
        print(f"current user is: {user}")
    return



#fullname = get_formatted_name('tony', 'montana')
#print(fullname)


#print(get_formatted_name('tony', 'montana'))
#print(get_list_of_even_numbers(20))
print(get_list_of_odd_numbers(23))

#print_username(['kamron'])
# Here it can be only 1 element, but must be a list


