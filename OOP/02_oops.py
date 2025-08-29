
#### --------------- OPERATOR OVERLOADING ---------------

####--------- Magic Methods (Dunder Methods)-----------

'''
__add__()
__sub__()
__mul__()

Dunder - Double UNDERscore
'''

a = 4
b = 2

print(a + b)
print(a.__add__(b))
print(int.__add__(2,3))
print(a.__eq__(b))


a = 'hello'
b = 'world'

print(str.__add__(a,b))
print(a.__add__(b))
print(a.__len__())
print(a.__str__())


'''
Operator overloading is used to change the behavior of an existing operator by redefining a special function that
is invoked when the operator is used with the objects.
'''

class X:

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def __add__(self,other):   
        print(self.name + other.name)
        print(self.age + other.age)
        print(self.place + other.place)

o1 = X('Sam', 25, 'Japan')
o2 = X('Pam', 29, 'Germany')

o3 = o1 + o2        

'''
To overcome this we can use __add__() for operator overloading.
When we use + operator, the magic method __add__ is automatically invoked
'''


### ---------------------------------------------------------------------------------

class X:
    def __init__(self, a,b):
        self.num1 = a
        self.num2 = b

    def __add__(self,other):
        print(self.num1 + other.num1)
        print(self.num2 + other.num2)

obj1 = X(2,3)
obj2 = X(5,5)
obj3 = obj1 + obj2


### ---------------------------------------------------------------------------------

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    ## This method is called when we use the '+' operator
    def __add__(self, other):
        """Defines the behavior for vector addition."""
        ## We create and return a *new* Vector object
        return Vector(self.x + other.x, self.y + other.y)

    ## This method provides a user-friendly string representation
    def __str__(self):
        """Called by print() and str() for a nice output."""
        return f"Vector({self.x}, {self.y})"

    ## This method provides an unambiguous representation for developers
    def __repr__(self):
        """Called for the object's official representation."""
        return f"Vector({self.x}, {self.y})"


## Let's create two vectors

v1 = Vector(2, 4)
v2 = Vector(3, 5)

## Now, we can use the '+' operator directly!
v3 = v1 + v2

print(v1)
print(v2)
print(f"The sum is: {v3}")

## The __repr__ is shown when you inspect the object in a shell
print(repr(v3))

### ---------------------------------------------------------------------------------

import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    ## --- New Methods Below ---

    ## Defines behavior for the '==' operator
    def __eq__(self, other):
        """Checks if two vectors are equal."""
        return self.x == other.x and self.y == other.y

    ## A helper method to calculate the magnitude (length)
    def __abs__(self):
        """Returns the magnitude of the vector, called by abs()."""
        return math.sqrt(self.x**2 + self.y**2)

    ## Defines behavior for the '<' operator
    def __lt__(self, other):
        """Compares vectors based on their magnitude."""
        return abs(self) < abs(other)

## --- Let's test them ---

v1 = Vector(3, 4)  ## Magnitude is sqrt(9 + 16) = 5
v2 = Vector(3, 4)
v3 = Vector(5, 12) ## Magnitude is sqrt(25 + 144) = 13

print(f"v1 == v2: {v1 == v2}")  ## Calls v1.__eq__(v2) -> True
print(f"v1 == v3: {v1 == v3}")  ## Calls v1.__eq__(v3) -> False
print(f"v1 < v3:  {v1 < v3}")   ## Calls v1.__lt__(v3) -> True
print(f"v3 < v1:  {v3 < v1}")   ## Calls v3.__lt__(v1) -> False
print(f"Magnitude of v1: {abs(v1)}") ## Calls v1.__abs__()



