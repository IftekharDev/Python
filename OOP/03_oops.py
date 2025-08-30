
#### ------------- METHOD OVERLOADING-------------------

# class xyz():
#     def add(self,a,b):
#         return a + b 

#     def add(self,a,b,c):
#         return a + b + c

# obj = xyz()

###print(obj.add(1,2))    ## Raises error as method overloading is not supported in python

# print(obj.add(1,2,3))


###------------------------------------------------------

# class wxyz():
#     def add(self,*args):         #Arbitrary Number of Arguments (alternative for method overloading)
#         total = 0
#         for i in args:
#             total = total + i
#         return total

# obj1 = wxyz()
# print(obj1.add(1,2,3,4,5))
# print(obj1.add(55,56,78,74,100))


###----------------Method Overriding---------------------------

# class Father:
#     def eat(self):
#         print("i eat healthy food")

#     def work(self):
#         print("i go to office")


# class Son(Father):
#     def eat(self):
#         print("i eat junk food")
#         super().eat()


# obj_son = Son()
# obj_son.eat()


# ----------------------------------------------------------------------

# class Parent:
#     def display(self):
#         print("Hello1")

#     def display(self,astring):
#         print("Hi!!",astring)


# class Child(Parent):
#     def display(self):
#         print("Hello2")

# p = Parent()

###p.display()          #raises an error as python doesn't support method overloading

# p.display("There")    

# c = Child()
# c.display()
