
class Human:
    name = 'Ben'
    age = 20
    address = 'Bhopal'

    def breath():
        return 'A Human breathes'


obj = Human()
print(Human.age)
print(Human.breath())


### --------------------------------------------------------------------

class Human:
    def __init__(self, name, age, ad):
        self.name = name
        self.age = age
        self.address = ad


obj1 = Human('Emma', 32, 'Bhopal')
print(obj1.name)


obj2 = Human('Tom')    # 3 arguments are required
print(obj2.name)


### --------------------------------------------------------------------------

class Human:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"I am {self.name}, I am {self.age} years old, and i live in {self.address}"

obj = Human("Emma", 13, "Delhi")
print(obj)


### --------------------------------------------------------------------------

class place:

    def __init__(self, name, famous):
        self.n = name
        self.f = famous

    def __str__(self):
        return f"{self.n} is famous for {self.f}"


p1 = place('Bhopal','Lakes')
print(p1)


#### ----------------- INHERITANCE -----------------
'''
It is a property of a class to inherit all the properties of another class
'''

## here we are defining a class A as parent class

class A:

    def method1(self):
        print("This is method1")

    def method2(self):
        print("This is method2")


'''
class B is the sub class/child class of class A. This is called multilevel inheritance
'''

class B(A):

    def method3(self):
        print("This is method3")


obj1 = A()
obj1.method1()
obj1.method2()


obj2 = B()
obj2.method1()          #this will raise an error unless you inherit class A to B
obj2.method3()


obj3 = A()             
###obj3.method3()       #this will raise an error

'''
it can be concluded that child class can inherit all the properties of parent/super class 
but a parent cannot inherit all the properties of child class
'''

### ---------------------------------------------------------------------------------

class Parent:

    def method_1(self):
        print("i am a method 1")

    def method_2(self):
        print("i am a method 2")


class Child(Parent):

    def method_3(self):
        print("i am a method 3")


obj = Child()
obj.method_1()

obj_Parent = Parent()
###obj_Parent.method_3()

