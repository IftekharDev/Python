
#### ----------- Arithmetic Operators in Python  ---------------

print(2+2)
print(2-2)
print(5*2)

x = 20
y = 2

print("addition: ",x+y)
print("subtraction: ",x-y)
print("multiplication: ",x*y)

print("division: ",x/y)    # normal division in python


###---------------------------------------------------------------


####  ---------------  modulo (%) -------------
'''
modulo gives you the remainder.
'''

x = 10
y = 3
print("remainder: ",x%y)


###---------------------------------------------------------------


#### ----------- floor divison in python(//)  ----------------
'''
floor gives you the quotient.
'''

print("quotient", 11//3)


###--------------------------------------------------------------


#### ---------- Comparison operators in Python  ---------------

'''
>   greater than operator 
<   less than operator
>=  greater than equal to
<=  less thaneq ual to
==  equal to operator
!=  not equal to operator
'''

a = 10
b = 6
print(a>b)  
print(a<b)  

print(a>=b)
print(a<=b)

print(a==b)
print(a!=b)

print(a==10)


###--------------------------------------------------------------


#### ----------- Raise to the power ---------------

print(2**2)      # prints the square of a number
print(2**3)      # prints the cube of a number

a = 4
b = 4
print(a**b)


###-------------------------Exercise-------------------------------------


num_1 = int(input('Enter a number: '))
num_2 = int(input("Enter another number: "))

print(num_1 + num_2)


###--------------------------------------------------------------


####  ------------    Logical Operators --------------


### -------------- and ---------------------
'''
returns True if both statements are true
'''

x = 6
y = 7
if (x == 6 and y == 7):
   print("yes")


####  ---------or -----------
'''
returns True if one of the statements is true
'''

x = 6
y = 7
if (x == 6 or y == 5):
   print("yes")


### ---------- not --------------
'''reverse the result, returns False if the result of statement is true.
'''

a = 2
b = 4
print(not a == 2)

print(a==2 and b==5)  
print(not(a==2 and b==5))


