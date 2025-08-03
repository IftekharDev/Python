
#### ---------- Local & Global variables in Python -------------

a = 10           ##global variable

def display():
   print(a)

display()


## --------------------------------------------------------------

def display():
   a = 15       ##local variable
   print(a)

display()
print(a)


## --------------------------------------------------------------

a = 20

def display_1():
   a = 21
   print(a)

display_1()
print(a)


#### ---------------- global keyword in python ------------------

a = 20

def display_1():
   global a
   a = 21
   print(a)

display_1()
print(a)



### ------------------ LAMBDA FUNCTION ------------------

'''
Lambda, also called as  "Anonymous" Function in Python. It is a one liner function
This function can have any number of arguments but only one expression.
'''

def add(x):
   return x + 5

print(add(5))

a = lambda x:x+5
print(a(5))


## -----------------------------------------------------------------------------------

my_func = lambda x:x*2
print(my_func(5))


## ----------------------------------------------------------------------------------

square = lambda x: x*x
print(square(5))


## ----------------------------------------------------------------------------------

string = "HAPPY"
function = lambda x: x.lower()

print(function(string))


## ----------------------------------------------------------------------------------

'''Even Number Using Lambda '''

z = lambda y:y%2 == 0
print(z(8))                                   #returns true


'''Odd Number Using Lambda '''

z = lambda x:x%2 != 0
print(z(13))


## ------------------Passing multiple arguments in lambda----------------------

'''Adding two numbers '''

z = lambda x,y:x+y
print(z(2,3))


'''Adding 3 numbers '''

z = lambda a,b,c:a+b+c
print("2 + 3 + 4 =",z(2,3,4))


'''Sorting list '''

li = [2,5,9,1,4,3,100,7]

sorted_list = lambda x: x.sort()
sorted_list(li)
print(li)


li = [2,5,9,1,4,3,100,7]

sorted_list = lambda x : sorted(x)
print(sorted_list(li))


## ----------------------------------------------------------------------------------

new_func = lambda x: 'even' if x %2 == 0 else 'not even'
print(new_func(8))

