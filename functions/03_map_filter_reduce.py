
#### -------------------- MAP FUNCTION -------------------------------

'''
Map function returns a map object. It takes two arguments, a function and an iterable.
It appplies a given function to each item of that given iterable.
'''

'''Returning a cube list using map '''

li = [1,2,3,4,5]

def cube(n):
    return n**3

cube_list = list(map(cube,li))
print(cube_list)


## ------------------------------------------------------------------------

list_of_strings = ['scissors', 'pen', 'bicycle', 'bottle']
number_li = []

def count_the_len(a):
    for i in a:
        number_li.append(len(i))

count_the_len(list_of_strings)
print(number_li)


len_list = list(map(len, list_of_strings))
print(len_list)


## ---------------------------------------------------------

'''Converting list of ints into list of string'''

int_list = [2,4,5,6,3,8]

string_list = list(map(str, int_list))
print("List Of Strings:",string_list)


## ----------------------------------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)


## ---------------------------------------------------------------------------------------

'''Adding two lists using map'''

alist = [1,2,3,4,5]
blist = [6,7,8,9,10]

added_list = list(map(lambda x,y: x+y, alist, blist))
print(added_list)


## ---------------------------------------------------------------------------------------

li = [1,2,'Hello', True, 7]

string_list = list(map(str, li))
print(string_list)


## ---------------------------------------------------------------------------------------

num = int(input("Enter a number to print cubes upto it: "))

cubes_list = list(map(lambda x: x**3, range(1,num+1)))
print(cubes_list)


#### --------------- FILTER FUNCTION -------------------
'''
Filter function filters out a given sequence by passing it into a function returning true values
'''

li = [1,2,3,4,5,6,7,8,9]
def evens (a):
    if a %2 == 0:
        return a

evensList = list(filter(evens,li))
print(evensList)


## ------------------------------------------------------------------------------------

li = [1,2,3,4,5,6,7]
z = lambda x: x%2==0
for i in li:
    print(z(i))

newEvenList = list(filter(lambda x: x%2==0,li))
print(newEvenList)

odds = list(filter(lambda x:x%2 != 0, li))         #filter odds from a list
print("List of Odd:",odds)


## ------------------------------------------------------------------------------------

a = [1,2,3,4,5]
b = [2,3,4,6,7]
n = list(filter((lambda x: x in a),b))
print(n)


## ------------------------------------------------------------------------------------

'''
numbers divisible by 5
'''

alist = [2,3,5,6,8,10,11,15,17,25,34,35,40,7,8,12,55]
y = list(filter(lambda x: x%5 == 0, alist))
print(y)



#### ---------------- REDUCE FUNCTION--------------------
'''
Reduce function passes a given sequence to a function and reduces it to a single value
'''

from functools import reduce

alist = [2,3,5,5,6]
sumlist = reduce(lambda x,y:x+y, alist)
print (sumlist)

def element_printer(x,y):
    print("x = ", x, " y = ", y)
    return x+y

sumlist = reduce(element_printer, alist)
print(sumlist)


## ---------------------factorial using reduce----------------------

num = int(input("Enter a number to calculate its factorial: "))

factorial = reduce(lambda x, y: x*y, range(1,num+1))
print(factorial)


## ----------------------------------------------------------

numbers = [5,8,7,3,2,10,1,9]

print(reduce(lambda a,b: a+b, numbers))


## ----------------------------------------------------------

# question :
products = [{"name":"mobile","price":499},
                   {"name":"shirt","price":899},
                   {"name":"book","price":399},
                   {"name":"mugs","price":999}]

print(list(filter(lambda x: x['price'] > 500, products)))



'''
2 - Write a Python program which selects and prints (as a list) all the strings of length greater than 4
from a list of strings using filter function and lambda(2 marks)
'''

strings = ['alexander','joe','tiffany','ana','max','george']

print(list(filter(lambda x: len(x)>4, strings)))

