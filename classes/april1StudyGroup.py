# 4/1/2021 Study Group

# 3 Functions examples
# Class and Object example with get/set functions examples


def describe_pet(pet_name):
    return(f"{pet_name.title()} is a dog")


def get_reverselist(nums):
    new_list = []
    n = len(nums)-1
    while n >= 0:
        new_list.append(nums[n])
        n -= 1
    return new_list


def get_sum_skip13(nums):
    sum = 0
    for n in nums:
        if n == 13:
            n = 0
        else:
            sum += n
    return sum


print(describe_pet('Jessi'))
print(get_reverselist([1, 2, 3, 4]))
print(get_sum_skip13([1, 13, 2, 4, 2]))




# Class and Object
# you declare object with class

class Computer:
    """docstring: This class defines a modern computer"""

    # Functions:
    def __init__(self, company, model, year, functionality, sn, price):
        """each parameter now have to do self.something"""
        self.company = company
        self.model = model
        self.year = year
        self.functionality = functionality
        self.sn = sn
        self.price = int(price)

    def get_description(self):
        """Describe most essential things of computer"""
        print(f"Your company of computer is: {self.company}")
        print(f"The serial number is: {self.sn}")
        print(f"The price is: {self.price}")

    def set_price(self):
        """Price will be changed for upgrades on computer"""
        self.price += 1000

    def get_new_price(self):
        print(f"New price will be: ${self.price}")


# Execution
# Define Objects with your Class now:
pc1 = Computer('apple', 'mac', '2021', '6gb RAM', '0000123', 2500)
pc2 = Computer('windows', 'lenovo', '2021', '6gb RAM', '0000123', 3500)


print("*** pc1 ***")
pc1.get_description()
pc1.set_price()
pc1.get_new_price()

print("*** pc2 ***")
pc2.get_description()
pc2.set_price()
pc2.get_new_price()
