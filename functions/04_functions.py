
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


#### ------------------- Decorator -------------------

def decorator(func):
    def wrapper():
        print("Hello World")
        func()
        print("Thanks for using decorator")
    return wrapper

@decorator
def greet():
    print("have a nice day!")

greet()


### -----------------------------------------------------------------

def add_sprinkle(cake):  
    def wrapper():
        print("sprinkles sprinkled!!")
        cake()
    return wrapper


@add_sprinkle
def cake1():
    print("here's your chocolate cake")


@add_sprinkle
def cake2():
   print("here's your vanilla cake")

cake1()
print()
cake2()


### -----------------------------------------------------------------

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@uppercase_decorator
def greet(name):
  return f"Hello, {name}"

print(greet("Pythonista"))


#### ------------Chaining Decorators and Passing Arguments----------------

def add_exclamation_decorator(func):
    """Adds an exclamation mark to the end of the result."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{result}!"
    return wrapper


def uppercase_decorator(func):
    """Converts the result to uppercase."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@add_exclamation_decorator
@uppercase_decorator
def greet(name):
  """Returns a simple greeting."""
  return f"Hello, {name}"


print(greet("Developer"))
print(add_exclamation_decorator.__name__)


#### ------------Decorators that Accept Arguments----------------

def repeat(num_times):  # 1. The outer function accepts the decorator's arguments
    def decorator_repeat(func):  # 2. This is the actual decorator
        def wrapper(*args, **kwargs):  # 3. This is the wrapper that executes the logic
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def say_whee():
  print("Whee!")

say_whee()

