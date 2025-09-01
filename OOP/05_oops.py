
#### ------------------- Access Modifiers -------------------

'''
Access Modifiers in Python are used to control the visibility and accessibility of class attributes and methods. 
There are three access modifiers: public, private & protected.
They help encapsulate data and maintain control over how attributes and methods are accessed and modified.

To make an instance variable protected, use prefix "_" (single underscore) to it.

To make an instance variable private, use prefix "__" (double underscore) to it.
'''


# class Animal:
#     def __init__(self, name):
#         self._name = name         #Protected attribute


# class Cat(Animal):
#     def meow(self):
#         return f"{self._name} says Meow!"
    

# my_cat = Cat("Kitty")
# print(my_cat.meow())

# print(my_cat._name)  # possible but not recommended

# Animal = Animal("hola")
# print(Animal._name)

# my_cat._name = "snowie"
# print(my_cat.meow())   # again, not a good practice


### --------------------------------------------------------------------

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private attribute

#     def get_balance(self):   #Public method to access private attribute
#         return self.__balance


# account = BankAccount(1000)
# print(account.get_balance())

# ###print(account.__balance)     ## not possible to access a private attribute directly

# account.__balance = 2000        ##not possible
# print(account.get_balance())

# print(account._BankAccount__balance)    ## name mangling
# account._BankAccount__balance = 8000
# print(account._BankAccount__balance)



### --------------------------------------------------------------------

# class Employee:
#     def __init__(self, name, age, salary):
#         self._name = name                   # protected instance attribute
#         self.__age = age                    # private instance attribute
#         self.salary = salary

#     @property
#     def ageMethod(self):
#         return self.__age

# emp = Employee("Ana", 30, 40000)

##print(emp.__age)   #gives an error

# print(emp.ageMethod)       # accessing age using getter

##emp.ageMethod = 21
# print(emp.ageMethod)


#### ------------Encapsulation - GETTER / SETTER------------------------

'''
Getter and Setter methods in python are used to provide read
'''

# class Employee:
#     def __init__(self, name = 'abc', age = 50, salary = 500):
#         self.name = name
#         self.__age = age
#         self.__salary = salary
        
#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self,value):
#         self.__age = value
    
#     @property
#     def salary(self):
#         return self.__salary

#     @salary.setter
#     def salary(self, value):
#         self.__salary = value


# obj = Employee()
# print(obj.age)

# obj.age = '10'  
# print(obj.age)

##print(obj.__salary)       ##can't access a private attribute directly

# print(obj.salary)
# print("Previous Salary:", obj.salary)

# obj.salary = 10             ## now the salary can be updated, with the help of setter method.
# print("Updated Salary :",obj.salary)


