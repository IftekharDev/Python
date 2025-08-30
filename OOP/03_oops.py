
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


### ----------------------------------------------------------------------

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


### ----------------------------------------------------------------------

# class Father:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house


# class Son(Father):
#     pass


# objDad = Father("henry","1 house")
# print(objDad.name)

# obj = Son("jerry", "a house")
# print(obj.name)


### Practice Question: 

'''
Q. Define a class named Book with three attributes: title, author & pages.
Implement a method called description() that returns a string representation of the class.
'''

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f"{self.title} is written by {self.author} and it has {self.pages} pages"
    

# ice_and_fire = Book("Ice And Fire","George RR Martin", 900 )
# print(ice_and_fire)


# -----------------------------------------------------------

# class Parent:
#    def display(self):
#        print("Hello1")

#    def display(self,a):
#        print("Hi!!",a)


# class Child(Parent):
#    def display(self,a = None):
#        print("Hello2")
#        super().display(a)   


# c = Child()
# c.display()
# c.display("there")


### ------------------------------------------------------------

'''
Q. Define a class named Student with three attributes: name, student_id, and grade.
Implement a method called get_info() that returns a string representation of the class.
Then, define a subclass named Undergraduate that inherits from Student 
and includes two additional attributes: major and year.
Implement a method called get_details() that returns a string 
representation of the Undergraduate class, including all attributes.
'''


# class Student:
#     def __init__(self, name, student_id, grade):
#         self.name = name
#         self.student_id = student_id
#         self.grade = grade

#     def get_info(self):
#         return f"Hiii I'm {self.name}, my student id is {self.student_id} and My grade is {self.grade}"
    

# class Undergraduate(Student):
#     def __init__(self,name, student_id, grade, major, year):
#         super().__init__(name, student_id, grade)
#         self.major = major
#         self.year = year

#     def get_details(self):
#         return f"Hiii I'm {self.name}, my student id is {self.student_id} and I'm in grade {self.grade}. I'm doing major in {self.major} and I'm in year {self.year}"
    

# obj = Undergraduate("Zain", 101, "A", "CSE", 2025)
# print(obj.get_details())
# print(obj.get_info())

