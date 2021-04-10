# 03/28/2021 OOP
# Class and Objects

# Chapter 9
# don't put anything executable in a specifically class file

class Car:
    """This class describes model of the car"""

    def __init__(self, brand, model, color):
        """this is a constructor, with required parameters."""
        self.brandofthecar = brand
        self.modelofthecar = model
        self.colorofthecar = color
        self.__odo_reader = 0 # also a gobal variable, but we dont require it to be passed as parameter
        # using encapsulation(__odo_reader), to hide data
        # from object(users) on the outside

    def set_odometer_reader(self, miles: int):
        """will not return anything, will just update the value"""

        # input control: check if entered number is a positive integer
        if miles > 0:
            self.__odo_reader = miles
        else:
            return 1



    def get_description(self):
        print(f"Brand of the car: {self.brandofthecar}")
        print(f"Model of the car: {self.modelofthecar}")
        print(f"Color of the car: {self.colorofthecar}")
        print(f"You have {self.__odo_reader} miles on your car")


    def drive(self):
        """driving action/ behavior"""
        if self.brandofthecar.lower() == 'bmw':
            print(f"You are driving FAST car plus no DL!")
        else:
            print(f"You are driving the car even without DL! isn't it awesome!")


    def do_something(self):
        print("I want to do something ......")
        print("let me drive this car :) ")
        self.drive()
        #motor = Motorcycle()
        #motor.drive()

def greet_user():
    print("* hello car enthusiast *")

class ElectricCar(Car):
    """This is child class of Car() class. ElectricCar class inherits from Car class"""

    def __init__(self, brand, model, color):
        """this is a constructor, with required parameters."""

        #   now this is for electric car init
        #   passing here whatever we received from object/ Increased re-usability
        super().__init__(brand, model, color)
        self.battery_size = 100

    def get_battery_info(self):
        print(f"This car has a {self.battery_size}-- kWh battery.")

    def get_description(self):
        """This overwrites the parent function"""
        super().get_description()
        print(f"battery size of the car: {self.battery_size} ")
