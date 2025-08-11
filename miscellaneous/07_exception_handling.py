
# -------------- Exception Handling --------------

'''
An exception in Python is an incident that happens while executing a program. 
When a Python program meets an error, it stops the execution of the rest of the program. 
When a Python code comes across a condition it can't handle, it raises an exception.

In Python, we catch exceptions and handle them using try and except code blocks. 
The try clause contains the code that can raise an exception, 
while the except clause contains the code lines that handle the exception.

There is another block finally that is optional and is used for code that must be 
executed regardless of whether an exception occurred or not.
'''

# ----------------------------------------------------

'''
Any number divided by zero raise a zero division error and the error can be handled by raising an exception
'''

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))

# try:
#    print(num1/num2)

# except Exception as e:
#    print("This operation is incorrect :", e)


# -------------------------------------------------------

# n1 = int(input("enter a number: "))
# n2 = int(input("enter a number: "))

# try:
#    print(n1/n2)

# except ZeroDivisionError as error:
#    print("incorrect programme", error)

# print("Programme terminated")


# -------------------------------------------------------

# num1 = input("enter 1st num: ")
# num2 = input("enter 2nd num: ")

# try:
#    print("Start of a program")
#    print(int(num1)/int(num2))

# except Exception as e:
#    print("This is invalid :", e)

# finally:
#    print("End of Program")

# print("Program Terminated")


# ----------------------------------------------------------

# def weight(n):
#    try:
#        return int(n)
#    except Exception as ex:
#        print(ex)

# w = weight('ten pounds')
# print(w)


# ----------------------------------------------------------

# def weight(n):
#     try:
#         return int(n)
#     except ValueError as ex:
#         print('value error',ex)

# w = weight('10')
# print(w)


##----------Different types of exceptions in python-------------------------

'''
SyntaxError, TypeError, NameError, IndexError, KeyError, ValueError, AttributeError, 
#IOError, ZeroDivisionError, ImportError, RuntimeError, OSError and more.
'''

'''
Q.1 - Write a Python function that divides two numbers and handles the division by zero exception.
'''

# def divide(a ,b):
#     try:
#         division = a/b
#         return division
#     except ZeroDivisionError as e:
#         return "Can't divide a number by zero."
#     except Exception as e:
#         return f"An error occured - {e}."
    
# print(divide(17,0))
# print(divide(928, 'as'))


# ---------------------------------------------------------------------------------------------

'''
Q.2 - Write a Python function that reads from a file and handles the file not found exception.
'''

# def read(path):
#     try:
#         with open(path, 'r') as var:
#             return var.read()
#     except FileNotFoundError as e:
#         return f"File not found - {e}."
#     except Exception as e:
#         return f"An unknown error occured {e}"
    
# print(read("text.txt"))


# ---------------------------------------------------------------------------------------------

'''
Q3. - Write a Python function that takes a string and converts it to an integer. 
      Handle the case where the conversion fails due to invalid input.
'''

# def integer(str):
#     try:
#         return int(str)
#     except ValueError as e:
#         return f"Invalid value to convert it to integer. - {e}"
#     except Exception as e:
#         return f"An unknown error occured {e}"
    
# print(integer('64276'))
# print(integer('32h73m'))


# ---------------------------------------------------------------------------------------------
  
'''
Q4. - Write a Python function that retrieves an element from a list by its index. 
      Handle the case where the index is out of range.
'''

# def get_element(lst, index):
#     try:
#         print( lst[index])
#     except IndexError:
#         print( "Error: Index is out of range.")
#     except Exception as e:
#         print( f"An unexpected error occurred: {e}")

# my_list = [1, 2, 3, 4]
# get_element(my_list, 2)
# get_element(my_list, 10)


# ---------------------------------------------------------------------------------------------
  
'''
Q.5 - Write a Python function that performs multiple operations: division, file
      reading, and string conversion. Handle multiple types of exceptions that may arise.
'''

# def multiple_work(num1, num2, file, s):

#     try:
#         div = num1/num2
#         with open(file, 'r') as text:
#             all_text = text.read()
#         integer = int(s)
#     except ZeroDivisionError as e:
#         return "Can't divide a number by zero."
    
#     except FileNotFoundError as e:
#         return f"File not found - {e}."
    
#     except ValueError as e:
#         return f"Invalid value to convert it to integer. - {e}"
    
#     except Exception as e:
#         return f"An unknown error occured {e}"
    
#     else:
#         return div, all_text, integer
    
        

# print(multiple_work(23,4,'text.txt','12'))
# print(multiple_work(23,0,'text.txt','12das'))


#### -----------------Math Module-----------------------------------

# import math

# print(dir(math))

# print(math.factorial(5))

# result = math.sqrt(16)
# print(result)


# print(math.pi)

# a, b = 60, 48
# result = math.gcd(a,b)
# print(f"GCD of {a} and {b} is {result}")
        