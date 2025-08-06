
#### ---------------- KEY SORTING ------------------

'''
Key sorting means to sort an iterable on the basis of any property of items within that iterable
'''

'''
The sorted() function and the .sort() method are commonly used for this purpose in Python. 
Both can take a key parameter, which is a function that 
specifies how the elements in the collection should be compared.
'''

'''
sorted(): Returns a new sorted list from the elements of any iterable.
.sort(): Sorts the list in place and returns None.
'''


aList = [9,4,2,5,6,7,8]                                                # normal sorting
bList = sorted(aList)
print(bList)


li = [9,4,2,5,6,7,8]                                                # sorting in descending order
new_li = sorted(li, reverse=True )
print(li)
print(new_li)


fruits = ["Apple", "Pineapple", "Pear", "Banana"]
print(sorted(fruits))
print(sorted(fruits, reverse=True))


#---------------------------------------------------------------------------------

list_of_tuples = [('a', 4),('z',1),('b',3),('n',7),('c',8)]
sorted_list = sorted(list_of_tuples)
print(sorted_list)
print(list_of_tuples[2][1])


list_of_tuples = [('a', 4),('z',1),('b',3),('n',7),('c',8)]
my_func = lambda x: x[1]

sorted_li = sorted(list_of_tuples, key = my_func)
print(sorted_li)


# ---------------------------------------------------------

fruits = ["Apple", "Pineapple", "Pear", "Banana"]

def func(elem):
    return len(elem)

print(sorted(fruits))
print(sorted(fruits, key = func))
print(sorted(fruits, key = func, reverse = True))
print(sorted(fruits, reverse=True, key=func))

print(sorted(fruits, key = lambda elem : len(elem)))
print(sorted(fruits, key = lambda elem : len(elem), reverse = True))
print(sorted(fruits, key=len, reverse=True))


# ---------------------------------------------------------

## Sort by a specific key in each dictionary.

data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)


#### ------------------------ .sort() --------------------------------------

my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

# ---------------------------------------------------------

words = ['banana', 'kiwi', 'Raspberry', 'apple']
words.sort(key=len)   
print(words)                       
           
words.sort(key=len, reverse = True)
print(words)


'''
Q. Sort the people list by the length of each person's name in descending order.(use sort function )
'''

people = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Ana', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
    {'name': 'Diana', 'age': 28, 'city': 'Miami'}
]

people_1 = sorted(people,key= lambda x: len(x['name']), reverse=True)
print(people_1)


'''
Q. sort the given list of items on the basis of their prices in descending order.
'''

items = [{'product': 'Book', 'price': 15.99},
        {'product': 'Laptop', 'price': 999.99},
        {'product': 'Pen', 'price': 1.99}]

sorted_items = sorted(items, key = lambda x: x['price'], reverse= True)
print(sorted_items)

