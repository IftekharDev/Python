
#### ---------Assignment operator----------------

'''
In Python, the assignment operator (=) does not create a copy of the object. 
Instead, it creates a new reference to the same object.
'''

a = [4,5,6,7,8]
b = a
b[0] = 3

print(b)
print(a)

'''
id() returns unique identification value of the object stored in memory.
'''

print(id(b))
print(id(a))


#### ------------------------- Shallow copy ----------------------------------

'''
A shallow copy created using .copy(), copies the outer elements but not the nested objects.
.copy() creates a shallow copy in Python.
'''

li = [1,2,3,[4,5]]
li_2 = li.copy()

print(li)
print(li_2)
print(li == li_2)
print(li is li_2)
print(id(li))
print(id(li_2))

li_2[1] = 100
print(li)
print(li_2)

li_2[3][1] = 'a'
print((li))
print(li_2)

print(id(li[0]))
print(id(li_2[0]))
print(id(li[3]))
print(id(li_2[3]))

print(id(li))
print(id(li_2))

print(id(li[3]))
print(id(li_2[3]))


#### ----------------- Shallow Copy using module 'copy' --------------------------------

import copy

list_1 = [1,2,3,[4,5]]
list_2 = copy.copy(list_1)

list_2[0] = "apple"
print(list_1)

list_2[3][0]= "apple"
print(list_1)


#### --------------- Deep copy in Python -----------------------

'''
A deep copy created using copy.deepcopy(), copies both the outer list and all nested objects.
copy.deepcopy() is used to create a deep copy in python.
'''

import copy 

list_1 = [1,2,3,[4,5]]
list_2 = copy.deepcopy(list_1)

print(list_1)
print(list_2)

list_2[0] = "apple"
print(list_1)

list_2[3][0]= "apple"
print(list_1)
print(list_2)

print(id(list_1))
print(id(list_2))

print(id(list_1[3]))
print(id(list_2[3]))