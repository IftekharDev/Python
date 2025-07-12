
#### ----------Tuples ------------------

'''
In Python, a tuple is another built-in data type like list and dictionaries.
Tuples are immutable.
They are ordered(Indexed) and allow duplicate values.
Tuples can contain elements of different data types, such as integers, floats, strings, or even other tuples.
One can access individual elements of a tuple using indexing, similar to the list.
'''
 
# my_tuple = (1, 2, 3, 'a', 'b', 'c')

# print(my_tuple)
# print(my_tuple[0])
# print(my_tuple[3])
# print(my_tuple[5])
# print(my_tuple[1:2])

# print(my_tuple.index('a'))
# print(my_tuple.index(1))
# print(my_tuple.index('c'))


#### ---------------------------------------------

# new_tup = (1)
# print(new_tup)
# print(type(new_tup))

# new_tup_1 = (1,)  ## To make a single element tuple it's necessary to add , after the element.
# print(type(new_tup_1))


#### -------count() in tuple--------------------

# tup = (2,4,5,3,1,2,7,6,2,8,2)

# print(tup)
# print(len(tup))

# print(tup.count(2))
# print(tup.count(7))


#### -------del in tuple------------------------

# tup = (2,4,5,3,1,2,7,6,2,8,2)
# del(tup)
# print(tup)


#### -------joining tuples----------------------

# my_tuple = (1, 2, 3, 'a', 'b', 'c')
# tup = (2,4,5,3,1,2,7,6,2,8,2)

# newTup = my_tuple + tup
# print(newTup)
# print(len(newTup))


#### -------converting a list into a tuple ----------

# alist = ['red','purple','pink','orange','yellow']
# print(alist)

# tup2 = tuple(alist)
# print(tup2)


#### --------converting a string into a tuple---------

# string = 'it\'s a brand new day!'
# print(string)

# tup3 = tuple(string)
# print(tup3)