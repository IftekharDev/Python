
#### ---------------- BREAK AND CONTINUE ----------------

'''
break statement is used to exit a loop when an external condition is met.
'''

for i in range(6):
   if i == 3:
       break
   print(i)
  


'''
Continue statement stops the current iteration of the loop.
'''

for i in range(10):
   if i == 5:
       continue
   print(i)

'''
Break statement stops the entire process of the loop. 
Continue statement only skips the current iteration of the loop.
'''

#---------------------------------------------------------------------------

'''
Question : WAP to print all the elements except 'WoElement' from alist.
'''

a_list = [3, 'apple', 5, "WoElement", 'papaya', 22, True]

for i in a_list:
    if i!= "WoElement":
        print(i)

for i in a_list:
    if i=="WoElement":
        continue
    print(i)

#---------------------------------------------------------------------------

numbers = (1,2,3,4,5,6,7,8,9)
even_sum = 0
odd_sum = 0

for i in numbers:
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i

print(f"Sum of all evens are {even_sum}")
print(f"Sum of all odds are {odd_sum}")

#---------------------------------------------------------------------------

'''
Q. WAP to find out the index value of "pineapple".
print the statement once you've find out the element 'i have found Pineapple on index _'
'''

fruits = ['apple', 'kiwi', 'orange', 'mango', 'papaya', 'pineapple','papaya']

index = 0

for i in fruits:
    if i!="pineapple":
        index+=1
    else:
        print(f"I've found Pineapple on index {index} ")
        break



fruits = ['apple', 'kiwi', 'orange', 'mango', 'papaya', 'pineapple','papaya']
num = 0
for i in fruits:
   if i=="pineapple":
       break
   num+=1
print("i have found pineapple on index", num)


fruits = ['apple', 'kiwi', 'orange', 'mango', 'papaya', 'pineapple','papaya']

for index, element in enumerate(fruits):
    if element=='pineapple':
        print(f"I've found Pineapple on index {index} ")
        break



#### ---------------- for else ----------------

'''
for Loop: Repeats code for each item in a sequence.
else Block: Runs after the for loop is finished executing, but only if the loop didn't end early with a break.
'''

for i in range(1,5):
   print(i)
else:
   print("Program completed")

#--------------------------------------------------

for i in range(6):
   if i == 3:
       break
   print(i)
else:
   print("successfully executed")

#--------------------------------------------------

for i in range(6):
   if i == 8:
       break
   print(i)
else:
   print("successfully executed")


#-------------------------------------------------------------

numbers = [2,3,5,-1,0,33]
for i in numbers:
   print(i)
   if i == 0:
       break      
else:
   print("Loop finished without a break")


'''
Question. WAP to check whether a number is prime or not
'''

number = int(input("Enter a number to check prime: "))

for i in range(2,number):
    if number%i==0:
        print(f"{number} is not a prime number")
        break
else:
    print(f"{number} is a prime number")


import math as m

number = int(input("Enter a number to check prime: "))
int_sqrt = m.floor(m.sqrt(number)) + 1

for i in range(2,int_sqrt):
    if number%i==0:
        print(f"{number} is not a prime number")
        break
else:
    print(f"{number} is a prime number")


#-------------------------------------------------------------

fruits = ['apple', 'kiwi', 'orange', 'papaya', 'pineapple','papaya','mango']

for i in fruits:
    if i == "mango":
        print("I've found mango.")
        break
else:
    print("I've not found mango.")


