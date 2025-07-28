
#### --------------for loop ----------------

'''
for loop is used to iterate over an iterable (i.e., list, dictionary, tuple, set or string)
It helps you repeat a set of instructions for each item in a collection, 
letting you do something with each item without having to write the same code over and over again.
'''

for i in range(10):
   print("Hello world")

#-------------------------------------------------

alist = ["apple","banana","papaya","orange"]

for i in alist:
   print(i)

#--------------------------------------------------
    
num = 12

for i in range(num):
   print(i)

#--------------------------------------------------

'''
Qs. WAP to print the square of each element of a list.
'''

li = [1,2,3,4,5]

for i in li:
    print(i**2)

#--------------------------------------------------

'''
Qs WAP to write a table of the user inputted number.
'''

user_number = int(input("Enter a number for its table: "))

for i in range(1,11):
    print(f'{user_number} * {i} = {user_number*i}')

#--------------------------------------------------

'''
Qs. Iterate over a list of numbers 1 to 10 print only even numbers using for loop
'''

list_1 = [1,2,3,4,5,6,7,8,9,10]

for i in list_1:
    if i%2==0:
        print(i)


# Practice questions:

'''
Question 1: WAP to print all the odd numbers within the given range.
'''

given_range = int(input("Enter a number to odd numbers within its range: "))

for i in range(given_range+1):
    if i%2!=0:
        print(i)

#---------------------------------------------------------------------------

'''
Question 2: WAP to calculate the sum of all the natural numbers till 10.
'''

sum = 0

for i in range(1,11):
    sum+=i

print(sum)

#---------------------------------------------------------------------------

'''
Question 3: WAP to print the factorial of a number.
'''

num = int(input("Enter a number to calculate its factorial: "))

factorial = 1

if num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial*=i
    print(f"Factorial of {num} is {factorial}")

#---------------------------------------------------------------------------

'''
Question 4 : The Fizz-Buzz Question 
'''

for i in range(1,21):
    if (i%3== 0) and (i%5==0):
        print(f"{i} - FizzBuzz")
    elif i%3==0:
        print(f"{i} - Fizz")
    elif i%5==0:
        print(f"{i} - Buzz")
    else:
        print(f"{i}")


#---------------------------------------------------------------------------

'''
Question 5 : WAP program which converts all the elements of given list to the 
string representation of their respective datatypes.
Input -  [1, 2.0, 3, 'apple', 5, 'papaya'] 
Ouput -  ['integer',' float', 'integer', 'string', 'integer', 'string']
'''

input_list =  [1, 2.0, 3, 'apple', 5, 'papaya'] 
output = []

for i in input_list:
    if type(i) == int:
        output.append("integer")
    elif type(i) == float:
        output.append("float")
    elif type(i) == str:
        output.append("string")

print(output)

