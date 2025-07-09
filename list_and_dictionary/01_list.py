
#### -----------List in python-----------

'''
In Python, lists are used to store multiple items in a single variable.
List items are indexed hence, ordered.
Lists are mutable, and allows duplicate values.
By default 1st item in a list has 0th index.
Lists in python are created using square [] brackets.
A list can contain different data types at the same time.
'''

li = [1,2,3,4,5]
print(li)
print(len(li))

fruits = ['apple','oranges','banana','mangoes','papaya']
print(fruits)
print(fruits[4])                                 #printing an element using it's index value
print(len(fruits))
print(type(fruits))


### A list containing different data types

alist = ['12',12,'apple',2.3,'60','fifteen',False]

print(alist[2])
print(type(alist))
print(type(alist[2]))
print(type(alist[6]))


#### --------------------- range function ----------------------

'''
You can use range to generate a sequence of numbers and convert it to a list. 
This is useful when you need a list of consecutive numbers.
'''

new_list = list(range(5))
print(new_list)
output = [0, 1, 2, 3, 4]

alist = list(range(1,10))
print(alist)
output = [1, 2, 3, 4, 5, 6, 7, 8, 9]

blist = list(range(1,21,2))                      # the 2 in the last will skip one element after each element.
print(blist)
output =[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

clist = list(range(1,21,3))                          # the 3 in last will skip two elements.
print(clist)


#### -------Combining two lists-----------------------------

a = ['Hello',12,'15',True,5.5,3]
b = [1,2,3,4,5,6,7]

c = a + b
print(c)


#### ----- printing an element multiple times---------------

animals = ['cat','dog','giraffe','peacock','fish']
print(animals[0]*5)
print(animals[3]*4)


#### ------Counting the occurance of an element-------------

fruits = ['apple','apple','apple','orange','papaya','apple']
print(fruits.count('apple'))
print(fruits.count('papaya'))


#### -------index() method------------------------------------

'''
The index() method returns the index of the first occurrence of the specified element.
'''

fruits = ['apple','apple','apple','orange','papaya','apple']
print(fruits.index('apple'))
print(fruits.index('orange'))


#### -------Use of "in" & "not in" keyword-------------------------------

'''
In Python, you can use the in keyword to check if an element is present in a list.
'''

my_list = [10, 20, 30, 40, 50]
print(30 in my_list)              # returns True
print(35 in my_list)              # returns False
print(60 not in my_list)         # returns True
print(10 not in my_list)         # returns False


#### -------Replacing List elements---------------------------

flowers = ['rose','marigold','daisy']
print(flowers)

flowers[0] = 'lavender'
print(flowers)
output = ['lavender', 'marigold', 'daisy']

flowers[2] = 'Sunflower'
print(flowers)


#### -------remove() method----------------------

'''
It is used to remove the first occurrence of a specified element from the list.
'''

flowers = ['rose','marigold',"rose",'daisy']
flowers.remove('rose')
print(flowers)


#### --------pop() method ------------------------

'''
In Python, the pop() method is a list method used to remove and 
return the last item from a list or an item at a specified index.
'''

flowers = ['rose','marigold','daisy']
flowers.pop()        # removes last element as index not specified.
print(flowers)

flowers.pop(1)       # will remove element present on 1st index.
print(flowers)

flowers = ['rose','marigold','daisy']
print(flowers.pop())


#### -------- del keyword in python---------------

flowers = ['rose','marigold','daisy','lavender','sunflower']
del flowers[2]
print(flowers)
del flowers                   ## Deletes the whole list
print(flowers)

#### --------- clear() method----------------------

'''
In Python, the clear() method is used to remove all elements from a list.
'''

flowers = ['rose','marigold','daisy','lavender','sunflower']
flowers.clear()
print(flowers)


#### --------- append() method---------------------

'''
In Python, the append() method is a built-in method for lists.
It is used to add an element to the end of an existing list.
The append() method modifies the original list in place and does not return a new list.
append takes one only arguement at a time.
'''

flowers = ['rose','marigold','daisy','lavender','sunflower']
flowers.append('lily')
print(flowers)

flowers.append('tulip')
print(flowers)


#### --------- insert() method--------------------

'''
It is used to insert an element at a specified position(index) within a list.
insert() takes 2 arguments (index, element)
syntax :
insert(index, elements)
'''

flowers = ['rose','marigold','daisy','lavender','sunflower']
flowers.insert(0, 'dandelion')
print(flowers)


#### ---------- extend() method--------------------

'''
In Python, the extend() method is a built-in method for lists.
It is used to append elements to the end of an existing list.
'''

flowers = ['rose','marigold','daisy','lavender','sunflower']
flowers2 = ['dandelion','jasmine','Hibiscus','Bougainvillea']
flowers.extend(flowers2)
print(flowers)