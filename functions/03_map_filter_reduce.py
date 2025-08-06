
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

