
#### ----------- use of .clear() ---------------------------

'''
In Python, the .clear() method is used to remove all elements from a mutable sequence, 
such as a list, set, or dictionary.
'''

my_dict = {
    'name':'Ben',
    'age':'11',
    'city':'New york'}

my_dict.clear()
print(my_dict)


#### ----------- use of .pop()------------------------------

'''
The dict.pop() method is used to remove a key and it's value from a dictionary.
'''

my_dict = {
    'name':'Ben',
    'age':'11',
    'city':'New york'}
my_dict.pop('age')
print(my_dict)



#### ------------- empty dictionary -------------------------

emp_dict = {}   # creating an empty dictionary
print(emp_dict)
print(len(emp_dict))


#### --------------Deleting a dictionary ------------------------

my_dict = {
    'name':'Ben',
    'age':'11',
    'city':'New york'}

del(my_dict)
print(my_dict)


#### ------------- .copy() -------------------------

fruits = {
    1:'apple',
    2:'banana',
    3:'pineapple',
    4:'mango',
    5:'papaya'}

print(fruits)

dict2 = fruits.copy()
print(dict2)
print(dict == dict2)




#### ------------------------- NESTED DICTIONARY -----------------------

'''
A nested dictionary in Python is simply a dictionary that contains another dictionary as its value. 
This can be useful for storing more complex data structures.
'''

pets = {
    "pet1": {"name": "Buddy", "type": "dog", "age": 5},
    "pet2": {"name": "Mittens", "type": "cat", "age": 3},
    "pet3": {"name": "Tweety", "type": "bird", "age": 2}
}

print(pets)
print(pets["pet1"])
print(pets["pet1"]["age"])

pets["pet2"]["age"] = 4
print(pets)


#### ------------------------- Practice Ques -----------------------

student_data = {
    "Student_1" : {"Name":"xyz", "age": 18},
    "Student_2" : {"Name":"abc", "age": 78},
    "Student_3" : {"Name":"something", "age":20}
    }

print(len(student_data))
print(student_data["Student_1"]["age"])

### change the name of student_2
student_data["Student_2"]["Name"] = "Shahrukh"
print(student_data)

### Add address for student_3
student_data["Student_3"]["Address"] = "Batla House"
print(student_data["Student_3"])

### Delete the address of student_3.
del student_data["Student_3"]['Address']
print(student_data["Student_3"])


Teams = {
    "Team_A" : ["Nora", "Salman"],
    "Team_B" : ["Zadran", "Irshad"],
    "Team_C" : ["John", "Salena"]
     }
print(Teams["Team_C"])
Teams["Team_B"].append("Saba")
print(Teams)

Teams["Team_B"].pop()

print(Teams)


my_dict = {
        "obj_1" : "i am a dictionary",
        "obj_2" : {"key_1":"i am a dictionary within a dictionary"},
        "obj_3" : ["apple","banana","mangoes",["papaya","orange"]],
        "obj_4" : {"key_2": {"Greetings":"Hello World"}},
        "obj_5" : {"key_3": [1,2,3]}
        }

# Q.1, WAP to print Hello World from obj_4
# Q.2, WAP to print Orange from obj_3
# Q.3, WAP to add 4 as a last element in the list, present inside obj_5
# Q.4, WAP to add a new key and value in your dictionary "obj_6" containg boolean values 
#           in a list as the key's valuse. example ;          {"obj_6" : [True, False]}
# Q.5, replace "mangoes" from obj_3 with "kiwi"


print(my_dict["obj_4"]["key_2"]["Greetings"])

print(my_dict["obj_3"][3][1])

my_dict["obj_5"]["key_3"].append(4)
print(my_dict["obj_5"]["key_3"])

my_dict["obj_6"] = [True , False]
print(my_dict["obj_6"])

my_dict["obj_3"][2] = "kiwi"