
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



