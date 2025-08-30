
####---------------- Duck Typing -------------------------

'''
In Python, where the type of an object is determined by its behavior (methods and properties) 
rather than its explicit type. If it walks like a duck and quacks like a duck, it must be a duck.
'''


# class Bird:
#     def fly(self):
#         return "a bird flies in the sky"


# class AirPlane:
#     def fly(self):
#         return "AirPlane flies in the sky"


# def make_it_fly(flyable_object):
#     return flyable_object.fly()

# sparrow = Bird()
# jet = AirPlane()
# make_it_fly(sparrow)
# make_it_fly(jet) 


'''
Here, both Bird and Airplane have a fly() method, and the make_it_fly() function 
works with any object that has a fly() method, regardless of the object's actual class.
'''

###---------------------------------------------------------

# class Duck:
#     def quack(self):
#         print("Quack, quack!")

#     def fly(self):
#         print("Flap, flap!")


# class Person:
#     def quack(self):
#         print("I'm quacking like a duck!")

#     def fly(self):
#         print("I'm waving my arms and pretending to fly!")


# This function doesn't care about the type of the object.
# It only cares that the object has 'quack' and 'fly' methods.
# def make_it_quack_and_fly(thing):
#     try:
#         thing.quack()
#         thing.fly()
#     except AttributeError as e:
#         print(f"This object can't do that: {e}")

# Create instances of our classes
# donald = Duck()
# john = Person()

# print("Calling the function with a Duck:")
# make_it_quack_and_fly(donald)

# print("\nCalling the function with a Person:")
# make_it_quack_and_fly(john)


####---------------- Abstract Class -------------------------

'''
Abstract Class - An abstract class is a class that cannot be instantiated directly but it can be inherited.
Abstract methods, on the other hand, are methods declared within an abstract class but without any implementation.
'''

# class Vehicle:
#     def drive(self):
#         pass

# obj = Vehicle()
# print(obj)

### this is working normally as Vahicle isn't an abstract class yet


###------------------------------------------------------------------

# from abc import ABC, abstractmethod           ##abstract base classes

# class Vehicle(ABC):
#     @abstractmethod
#     def drive(self):
#         pass

###obj = Vehicle()             ## can't be initiated
###print(obj)


# class Car(Vehicle):
#     def drive(self):
#         return "Car is being driven on the road."

# class Airplane(Vehicle):  
#     def drive(self):
#         return "The Airplane is flying in the sky."
    
# objCar = Car()
# print(objCar.drive())
# objAirplane = Airplane()
# print(objAirplane.drive())


###------------------------------------------------------------------

# No abstract Vehicle class here

# class Car:
#     def drive(self):
#         print("Car is being driven on the road.")

# class Airplane:
#     def fly(self):  # Uh oh, a different method name!
#         print("The Airplane is flying in the sky.")

# class Bicycle:
#     # This developer forgot to add any movement method!
#     def pedal(self):
#         print("Pedaling the bicycle.")

# def start_trip(vehicles):
#     print("--- Starting trip ---")
#     for vehicle in vehicles:
#         # This function EXPECTS every vehicle to have a .drive() method
#         vehicle.drive()
#     print("--- Trip finished ---")


# Let's create our fleet
# my_car = Car()
# my_airplane = Airplane()
# my_bike = Bicycle()

# # Let's try to start a trip with a car. This works fine.
# start_trip([my_car])

# # Now, what happens when we mix them?
# # This will CRASH!
# try:
#     all_vehicles = [my_car, my_airplane, my_bike]
#     start_trip(all_vehicles)
# except AttributeError as e:
#     print(f"\nERROR: The program crashed because of: {e}")


###------------------------------------------------------------------

# from abc import ABC, abstractmethod

# # The Contract: Anything that is a Vehicle MUST have a 'drive' method.
# class Vehicle(ABC):
#     @abstractmethod
#     def drive(self):
#         pass

# # This class follows the contract. It's a valid Vehicle.
# class Car(Vehicle):
#     def drive(self):
#         print("Car is being driven on the road.")

# # This class ALSO follows the contract. It's a valid Vehicle.
# # We force the developer to name the method 'drive'.
# class Airplane(Vehicle):
#     def drive(self):
#         print("The Airplane is flying in the sky.")

# # Now, let's see what happens when a developer makes a mistake
# class Bicycle(Vehicle):
#     # The developer forgot to implement the 'drive' method!
#     def pedal(self):
#         print("Pedaling the bicycle.")

# # The function is the same, but now it's SAFE.
# # It can TRUST that any object of type Vehicle will have a .drive() method.
# def start_trip(vehicles):
#     print("--- Starting trip ---")
#     for vehicle in vehicles:
#         vehicle.drive()
#     print("--- Trip finished ---")


# print("Creating a Car:")
# my_car = Car()
# print("Creating an Airplane:")
# my_airplane = Airplane()

# print("\nTrying to create a Bicycle...")
# try:
#     # This line will now FAIL IMMEDIATELY!
#     my_bike = Bicycle()
# except TypeError as e:
#     print(f"ERROR: Could not create Bicycle. {e}")

# # Since you can't even create a non-compliant object,
# # the start_trip function can never crash in this way.
# print("\nRunning a trip with the valid vehicles:")
# valid_vehicles = [my_car, my_airplane]
# start_trip(valid_vehicles)

