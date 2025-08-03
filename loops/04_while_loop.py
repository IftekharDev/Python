
#### ---------- while loop ---------------- 
''' 
used to repeat a set of actions or as long as a certain condition is true.
'''

i = 0           # initialization  

while i<10:           
   print(i)
   i += 1


## -----------------------------------------------------------------------------------

i = 5

while i >= 1:
   print(i)
   i -= 1



#### ----------------------------------- INFINITE LOOP ------------------------------------------------

'''
A while loop becomes an infinite loop when the condition it checks never becomes false.
'''

# while True:
#    print("Hello World")

##---------------------------------------------------------------------------

##i = 0
##
##while i < 5:
##    print(i)



##------------------- Practice Questions : --------------------------------


'''
print a table of a user inputted number using while loop.
'''

number = int(input("Enter a number for its table: "))

i = 1

while i<=10:
    print(f"{number} * {i} = {number*i}")
    i+=1


## ----------------------------------------------------------------------------

'''
print all the elements of the list using while loop.
'''

fruits = ["apple", "kiwi", "orange", "grape"]

i = 0

while i<len(fruits):
    print(fruits[i])
    i+=1


## ----------------------------------------------------------------------------

'''
factorial using while loop 
'''

num = int(input("Enter a number to cal its factorial: "))

i = 1
fact = 1

while i<=num:
    fact *=i
    i+=1

print(fact)




#### -----------------------------Break & Continue------------------------------------------------

count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break
else:
    print("loop successfully finished")



## ----------------------------------------------------------

i = 0

while i <5:
   if i == 3:
       i += 1
       continue
   print(i)
   i += 1


## -------------------------------

i = 0
while i < 5:
   print(i)
   i += 1
   if i == 9:
       break
else:
   print("loop successfully finished")


'''
printing a statement 10 times using while loop.
'''

i = 0

while i<10:
    print("Hello World!")
    i+=1


## ----------------------------------------------------------------------

'''
iterating over a list using while loop 
'''

alist = ["a", "b", "c", "d", "e"]

i = 0

while(i<len(alist)):
    print(alist[i])
    i+=1


## ----------------------------------------------------------------------

fruits = ["apple", "kiwi", "grape", "ffg"]

index = 0

while(index<len(fruits)):
    if fruits[index] == "orange":
        print(f"I've found the orange at {index+1}th position")
        break
    index+=1
else:
    print("I've not find the orange")


## ------------------------- Even Number question ------------------------------

max_number = int(input("Enter a max number to find evens up to it: "))

i = 1
evens = []

while(i<=max_number):
    if i%2==0:
        evens.append(i)
    i+=1

print(evens)


## ----------------------------------------------------------------------
'''
print 1 to 10 except 3 using while loop.
'''

i = 1

while i<=10:
    if i==3:
        i+=1
        continue
    print(i)
    i+=1


