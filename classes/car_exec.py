# this file for executing the cars.py classes

# Execution
# we create objects here. Objects: mycar, yourcar but only class: Car
from classes.cars import Car, ElectricCar

mycar = Car("BMW", "530xi", "black")
yourcar = Car("Lexus", "Lexus IS", "silver")


yourcar.drive()
mycar.drive()
mycar.get_description()
# mycar.odo_reader = 20
mycar.set_odometer_reader(60) # we put on some miles on the car
#mycar.__odo_reader = 30 # doesn't do anything
# can only alter this variables value from inside the class
mycar.get_description()

# print(mycar.__odo_reader) --> throws an attribute error
# because of encapsulation, meaning we cant access it from outside

print()
# 4/03/2021 EV sub-class (child class)
print("--- This is electric car instances ---")
my_ev = ElectricCar("tesla", "model x", "blue")
my_ev.get_description() #   we have access already
#    because we inherit attributes and behavior from parent class
#print(f"The battery size on ev is: {my_ev.battery_size}")
my_ev.get_battery_info()
# here you can see same f() get description is now coming from an eletric car child class
# We have overwritten (written on top of) the parent function
my_ev.get_description()



