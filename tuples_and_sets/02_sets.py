
#### ------------------- SETS IN PYTHON -------------------

'''
A collection of data which is unordered.
Sets are iterable, immutable and have no duplicate elements.
'''

colors = {'red','green','orange','purple'}
print(len(colors))
print(type(colors))

print("grey" in colors)                                   # returns False, as grey is not present in colors.
print("grey" not in colors)                             # returns True, as the statement is true.

for i in colors:
    print(i)


#### ------------------Adding element--------------------------------------

'''
adding element to set
'''
x = {'hello','world',2,'5',True}

x.add(10)
print(x)



#### --------Union And Intersection of Sets--------------

set1 = {2,3,4,5,7,8,9}
set2 = {4,5,6,7}

print(set1)
print(set2)

'''
union gives you all the elements of two or more sets without any duplicates.
'''
print('Union of sets:',set1 | set2)


'''
The intersection of sets in Python is used to find the common elements between two or more sets.
'''
print('Intersection of sets:',set1 & set2)


#### ---------------Subtraction of Sets-------------------------

set1 = {2,3,4,5,7,8,9}
set2 = {4,5,6,7}

print('set1 - set2', set1-set2)
print('set2 - set1', set2-set1)


#### ---------clearing sets----------------

set1 = {2,3,4,5,7,8,9}
set1.clear()
print(set1)


#### -------------creating an empty set--------------

emptySet = set()
print(emptySet)
print(type(emptySet))