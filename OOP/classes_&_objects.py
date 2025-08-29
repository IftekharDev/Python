
# class Human:
#     name = 'Ben'
#     age = 20
#     address = 'Bhopal'

#     def breath():
#         return 'A Human breathes'


# obj = Human()
# print(Human.age)
# print(Human.breath())


### --------------------------------------------------------------------

# class Human:
#     def __init__(self, name, age, ad):
#         self.name = name
#         self.age = age
#         self.address = ad


# obj1 = Human('Emma', 32, 'Bhopal')
# print(obj1.name)


##obj2 = Human('Tom')    # 3 arguments are required
##print(obj2.name)


### --------------------------------------------------------------------------

# class Human:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def __str__(self):
#         return f"I am {self.name}, I am {self.age} years old, and i live in {self.address}"

# obj = Human("Emma", 13, "Delhi")
# print(obj)


### --------------------------------------------------------------------------

# class place:

#     def __init__(self, name, famous):
#         self.n = name
#         self.f = famous

#     def __str__(self):
#         return f"{self.n} is famous for {self.f}"


# p1 = place('Bhopal','Lakes')
# print(p1)

