############### if-else statements ###############

#These are decision making statements used to execute a block of code.
#if a condition is true, if part is executed, if a condition is false, else part is executed
#if a user wants to check multiple conditions, if-elif-else ladder is used. elif is executed only when the condition passed in if block is false
 

num1 = int(input("Enter a number : "))
if num1>10:
   print("Greater than 10")
elif num1==10:
   print("Number is 10")
else:
   print("Less than 10")


num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
if num1>num2:
   print(f'{num1} is greater than {num2}') 
elif num1<num2:
   print(f'{num2} is greater than {num1}')
else:
   print(f'{num1} and {num2} are equal')

#---------------------------------------------------------

num = 9
if num%2 == 0:
   print(f"{num} is an even number.")
else:
   print(f"{num} isn't an even number.")

#---------------------------------------------------------

age = int(input("enter your age: "))
if age>= 18:
   print("Eligable to vote")
else:
   print("not eligable to vote")


#---------------------------------------------------------
    
### To check whether a user input is positive, negative or zero

x = int(input("Enter a number : "))
if (x>0):
   print("Number is Positive")
elif (x==0):
   print("Number is Zero")
else:
   print("Number is Negative")


#---------------------------------------------------------


x = int(input("enter a number: "))
y = int(input("enter another number: "))
operator = input("enter an operator: ")

if operator == '+':
    print(x+y)

elif operator == '-':
    print(x-y)

elif operator == '*':
    print(x*y)

elif operator == '/':
    print(x/y)

else:
    print("invalid operator")


#---------------------------------------------------------

num1 = int(input('enter a number: '))
num2 = int(input('enter a different number: '))
num3 = int(input('enter a different number: '))

if num1>num2 and num1>num3:
   print(f"{num1} is the greatest number.")

elif num2>num3:
   print(f"{num2} is the greatest number.")

else:
   print(f"{num3} is the greatest number.")