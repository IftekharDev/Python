
####-------- Callback Function----------------

'''
A callback function in Python is a function that is passed as an argument to another function and
is executed inside that function.
'''

def function_1(func):
    return "i am function 1 " + func()

def function_2():
    return "i am function 2"

result = function_1(function_2)
print(result)


### -------------------------------------------------------------------------------

def greet(name, callback):
   message = f"Hello, {name}!"
   return callback(message)

def print_message(msg):
   print(msg)

greet("Alice", print_message)


#### ------------Nested Function------------------------

'''
A nested function is a function defined inside another function.
'''

def outer():
   x = 12
   def inner():
       print(x)
   
   inner()

outer()


### -------------------------------------------------------------------------------

def greet(name):
   def say_hello():
       print(f"Hello, {name}!")
   
   say_hello()

greet("Alice")


#### -----------------Closure---------------------

'''
A closure is a function that retains access to the variables from its enclosing scope, 
even after the enclosing function has finished executing.

For inner Function to be a closure, it needs to be returned from outerFunction and 
then called after outerFunction has finished executing.
'''

def outer_function(x):
   def inner_function(y):
       return x + y
   return inner_function

result = outer_function(10)
print(result(5))


### -------------------------------------------------------------------------------

def my_func(value):
   def multiply(number):
       return number * value
   return multiply

result = my_func(3)

print(result(5)) 
print(result(10))


### --------------------------------

def Greet(n):
     def Greet_2():
           return f"Hello {n}"
     return Greet_2

var = Greet("Ana")
print(var())


#### ------------------- RECURSION -------------------

'''
When a function calls itself it is known as recursion. 
Recursive functions render the code look simple and effective.
'''

def greet():
    print("Hello World")
    # greet()
    
greet()


#-------------------------------------------------------

### Factorial using recursion

def factorial(n):
    if n ==0 or n ==1:
        return 1
    
    return n* factorial(n-1)

result = factorial(5)
print(result)