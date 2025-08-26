
#### ----------------- Iterables ------------------

'''
An Iterable is basically an object that any user can iterate over. ex- a list or a tuple
'''

# alist = [2,4,6,8,10]
# print(alist)
# print(alist[2])
# print(alist[4])
# for i in alist:
#    print(i)


#### ----------------- Iterators ------------------

'''
An Iterator is an object that helps a user in iterating over another object. 
An iterator is generated when we pass an iterable to iter() method. It gives one value at a time.
iter( ) converts an iterable into an iterator.
'''

# alist = [2,4,6,8,10]
# x = iter(alist)
# print(x)              # returns an iterator object


'''
for accessing values from an iterator we use __next__() {dunder or magic methods}.
__next__() method is used for iterating. It returns the next item available for iteration.
'''

# print(x.__next__())

### "next()" is same as "__next__()"

# print(list(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
## print(next(x))        #this will raise a stop iteration error


### for loop can be used to access it

# for i in x:               # iterator prints a value only once
#    print(i)              # loop will start from second value

# print(next(x))              #this will raise a stop iteration error


#### -------------------- GENERATOR --------------------

'''
A generator is a special type of iterator that is defined using a function with yield statements. 
Generators simplify iterator creation by handling the iterator protocol. Generator creates iterator
'''

 

# def func():
#    yield "Hello"


# string = func()
# print(string)           #this will return a generator object

# print(string.__next__())
# or
# print(next(string))      # this returns the actual value

# for i in string:
#    print(i)
#    print(type(i))


#-------------------------------------------------------------

# def num():
#     yield 1               # we can use multiple yield in generator
#     yield 2
#     yield 3

# var = num()
# print(var.__next__())
# print(var.__next__())

# for i in var:
#     print(i)


# -------------------------------------------------------------

# def square(n):
#     sq = n*n
#     yield sq

# SQUARE = (square(2))
# print(SQUARE)
# print(SQUARE.__next__())


# def even():
#     i =1
#     while True:
#         yield i*i
#         i+=1

# even_num = even()
# print(even_num.__next__())
# print(even_num.__next__())


# def squares():

#    for i in range(2,10):
#        sq = i*i
#        yield sq


# square = squares()
# print(square)
# print(square.__next__())
# print(square.__next__())


# squareList =[]
# for i in square:
#    squareList.append(i)

# print(squareList)