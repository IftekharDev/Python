
#### ----------------------- Functions in Python  --------------------------

'''
In Python, a function is a block of reusable code that performs a specific task when it's called.
'''

def greeting():
   print("Hello World")

greeting()


## ------------------------------------------------------------

def greeting():
   print("Hello World")

print("Have a nice day!")
greeting()


## ------------------------------------------------------------

def greeting_1(n):
   print("Hello", n)

greeting_1("Arsalan")
greeting_1("Atif")


## ------------------------------------------------------------

def addition(a,b):
   print(a + b)

addition(3,4)


#### ---------------------- return keyword ---------------------

def subtraction(a,b):
   return a-b

result = subtraction(8,2)
print(result)

result_2 = subtraction(10,2)
print(result_2)


#### -------------- DEFAULT ARGUEMENTS ------------------


def add(a,b,c =2):
    return a + b + c

result = add(3,3,3)
print(result)

result_2 = add(3,3)
print(result_2)


## ----------------------------------------------------------------

def greeting(name = "User"):
    return f"Hello {name}"

x = greeting("Mariya")
print(x)

y = greeting()
print(y)


#### ------------------ KEYWORD ARGUMENTS  -----------------------

def my_function(fruit_1, fruit_2, fruit_3):
    return f"my favourite fruit is {fruit_3}"

a = my_function("apple","banana","orange")
print(a)

b = my_function(fruit_1 = "Orange", fruit_2 = "banana", fruit_3 = "apple")
print(b)


#### ----------- Arbitrary Positional Arguments (*args) -------------

'''
*args allows a function to accept any number of positional arguments.
'''

def print_numbers(*args):
    print(type(args))     ## tuple type
    for i in args:
        print(i)

print_numbers(1, 2, 3, 4, 5)


## ---------------------------------------------------------

def add(*args):
    result = 0
    for i in args:
        result += i
    return result

a = add(1,2)
print(a)

b = add(12,34,55)
print(b)

c= add(8,7,6,7,8,9,0)
print(c)



#### ------------ Arbitrary Keyword Arguments (**kwargs) ------------

'''
*kwargs allows a function to accept any number of keyword arguments.
'''

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")



#### ------------ random module ------------

import random

print(dir(random))

print(random.random())  ## Returns a floating-point number x such that 0 ≤ x < 1.

print(random.randint(1,10))  ## Returns a whole number N with a ≤ N ≤ b (both ends inclusive).

print(random.randrange(1,10))   ## 10 is exclusive

print(random.randrange(1,10,2))  ## random.randrange(start, stop, step), stop is exclusive

li = [10,20,30,40,50,60]
print(random.choice(li))

li = ['red', 'green', 'blue']
print(random.choice(li))   # might print 'green'

print(random.uniform(1,10))   ## Returns a floating number N where a ≤ N ≤ b

random.shuffle(li)
print(li)



#### ----- Guessing Game-------------

while True:
    wanna_play = int(input("Enter 1 to play or 0 to exit: "))

    if wanna_play == 0:
        break
    
    import random

    random_number = random.randint(1,10)
    guess_list = []
    for i in range(5):
        guess = int(input("Enter the guess between 1 to 10: "))

        if guess == random_number:
            print(f"Congratulations You've won! Your guess {guess} is correct.")
            break

        elif guess > random_number:
            print(f"Wrong guess! try a smaller number than {guess}")

        elif guess< random_number:
            print(f"Wrong guess! try a greater number than {guess}")


