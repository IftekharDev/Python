
#### ---------- LIST COMPREHENSIONS ----------

print([i for i in range(1,11)])


## Create a list of odd values

oddList = [i for i in range(1,21) if i%2 != 0]
print('Odd List:',oddList)


square_list = [i*i for i in range(1,21)]
print(square_list)


cube_list = [i**3 for i in range(1,11)]
print(cube_list)


##A list with table of two

table_of_two = [i*2 for i in range(1,11)]
print("Table of 2:",table_of_two)


cities = ["Madrid", "London", "New York", "Berlin", "Tokyo"]

filtered_cities = [i for i in cities if "o" in i]
print(filtered_cities)


flowers = ["rose", "tulip", "sunflower", "lily", "daisy"]
new_list = [i for i in flowers if i!= 'daisy']
print(new_list)


#### -------------- NESTED LISTS --------------

a =[[i] for i in range(4)]
print(a)

nested_list = [[i for i in range(1,4)] for i in range(4)]
print(nested_list)


li_2 = [[i for i in range(1,31) if i%10==0] for i in range(4)]
print(li_2)


#### ---------------DICTIONARY COMPREHENSIONS-------------------

'''
Like list comprehensions, Python  supports dict comprehensions,
which allow you to express the creation of dictionaries at runtime using a similarly concise syntax.
'''

## This one maps the numbers in a specific range to their cubes

CubeDict = {x:x**3 for x in range(1, 10)}
print(CubeDict)


## A dictionary from a list with months as values and their lengths as keys

month_list = ['January', 'Februaury', 'March', 'May', 'July']

new_dict = {len(i):i for i in month_list}
print(new_dict)
print(len(new_dict))


## --------------------------------------------------------------------------------

## Making changes to an original dictionary

price_dict = {'milk':40, 'meat':250, 'rice':80, 'wheat':100}

# increasedPrice = Rs. 30 per item

newPrice_dict = {k:v+30 for k,v in price_dict.items()}
print(newPrice_dict)


#### -------------- NESTED DICTIONARY --------------

## Dictionary with tables of 2,3,4

Tbl = {i:{j:i*j for j in range(1,11)}for i in range(2,5)}
print(Tbl)

