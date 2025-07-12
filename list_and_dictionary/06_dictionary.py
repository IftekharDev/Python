#### ---------- use of .items() ----------------------------

'''
items() returns a list of tuples where each tuple is a tuple of key-value pair.
'''

# my_dict = {
#     'name':'Ben',
#     'age':'11',
#     'city':'New york'}

# print(my_dict.items())

'''
Getting key and value separately using .items()
'''

# for k,v in my_dict.items():
#    print(k,v)


#### ----------- use of .clear() ---------------------------

'''
In Python, the .clear() method is used to remove all elements from a mutable sequence, 
such as a list, set, or dictionary.
'''

# my_dict = {
#     'name':'Ben',
#     'age':'11',
#     'city':'New york'}

# my_dict.clear()
# print(my_dict)


#### ----------- use of .pop()------------------------------

'''
The dict.pop() method is used to remove a key and it's value from a dictionary.
'''

# my_dict = {
#     'name':'Ben',
#     'age':'11',
#     'city':'New york'}
# my_dict.pop('age')
# print(my_dict)



#### ------------- empty dictionary -------------------------

# emp_dict = {}   # creating an empty dictionary
# print(emp_dict)
# print(len(emp_dict))


#### --------------Deleting a dictionary ------------------------

# my_dict = {
#     'name':'Ben',
#     'age':'11',
#     'city':'New york'}

# del(my_dict)
# print(my_dict)


#### ------------- .copy() -------------------------

# fruits = {
#     1:'apple',
#     2:'banana',
#     3:'pineapple',
#     4:'mango',
#     5:'papaya'}

# print(fruits)

# dict2 = fruits.copy()
# print(dict2)
# print(dict == dict2)




#### ------------------------- NESTED DICTIONARY -----------------------

'''
A nested dictionary in Python is simply a dictionary that contains another dictionary as its value. 
This can be useful for storing more complex data structures.
'''

# pets = {
#     "pet1": {"name": "Buddy", "type": "dog", "age": 5},
#     "pet2": {"name": "Mittens", "type": "cat", "age": 3},
#     "pet3": {"name": "Tweety", "type": "bird", "age": 2}
# }

# print(pets)
# print(pets["pet1"])
# print(pets["pet1"]["age"])

# pets["pet2"]["age"] = 4
# print(pets)


