
#### ------------------------------- Split() Function ----------------------------

'''
splits a string into a list based on the separator given 
'''

newStr = 'have a beautiful day !'
print(newStr.split())

variable = 'apple,mango,papaya'
print(variable.split(","))

variable_2 = 'monkey#horse#cat#dog'
print(variable_2.split("#"))



#### -------------------------------- Join() Function ----------------------------------

'''
converts a list into a string 
'''

alist = [ 'a', 'b', 'c', 'd', 'e' ]
a = ",".join(alist)
print(a)

alist = [ 'a', 'b', 'c', 'd', 'e' ]
a = "#".join(alist)
print(a)

mySeparator = "HELLO"
b = mySeparator.join(alist)
print(b)


#### -------------------------------- Strip Function ----------------------------------


'''
Strip function is used to remove any whitespace from the starting and from the ending of a string
'''

string = "  ava  "
print(string.strip())


'''
strip can also be used to remove a specific characters if mentioned specified in the code
'''

string_1 = "  ,,,!!!.... avta ....,,ttt"
print(string_1.strip(" ,.!t"))


#### -------------------- Replace Function ------------------------

name = "Noore Nabi"
newName = name.replace("Nabi","Alam")
print(name)
print(newName)


#### -------------------- Count Function --------------------------

'''
counts the accurance of a substring
'''

newStr = "papaya papaya banana papaya orange orange"

print(newStr.count('papaya'))
print(newStr.count('orange'))
print(newStr.count('banana'))
print(newStr.count("a"))


#### -------------------- startswith() Method --------------------

'''
The startswith() method checks if a string starts with specified pattern or not.
if it does, it returns True, otherwise returns False.
'''

string_1 = "Hello World!"
print(string_1.startswith('Hello'))
print(string_1.startswith('H'))
print(string_1.startswith('He'))
print(string_1.startswith('Hi'))
print(string_1.startswith("World"))


#### --------------------- endswith() Method ---------------------

string_1 = "Hello World!"
print(string_1.endswith('Hello'))
print(string_1.endswith('!'))
print(string_1.endswith('He'))
print(string_1.endswith('World'))
print(string_1.endswith('World!'))


#### --------------------- title() Method ------------------------

'''
The title() method converts the first letter of each word in a string to uppercase and the rest to lowercase.
'''

a = "hello world"
b = a.title()
print(a)
print(b)


#### --------------------- lower() Method ------------------------

'''
The lower() method converts all the letters of a string in lowercase.
'''

a = "HellO wOrlD"
b = a.lower()
print(a)
print(b)


#### --------------------- upper() Method ------------------------

'''
The upper() method converts all the letters of a string in uppercase.
'''

a = "HellO wOrlD"
b = a.upper()
print(a)
print(b)


a = "apple"
print(a.upper())

b = "BANANA"
print(b.lower())

c = "Hello"
print(c.lower())


#### --------------------- String Concatenation ------------------------

first_name = "xyz"
last_name = "Khan"
full_name = first_name + " " + last_name
print(full_name)


#### --------------------- Indexing ------------------------

string = "January"
print(string[0])
print(string[1])
print(string[2])
print(string[6])


#### -------index() method------------------------------------

'''
The index() method returns the index of the first occurrence of the specified element.
'''

string = "I'm whoever"
print(string.index("m"))


#### --------------------- type casting ------------------------

a = 5
b = str(a)
print(a)
print(b)
print(type(a))
print(type(b))


#### --------------------- len() function ------------------------

'''
len() returns the total number of characters in a string.
'''


string = "My name is Arsalan Shaami"
print(len(string))


#### -----------------------------------------------------------------


stri = " ,, ava ,"
print(stri.strip(" ,"))

stri = " ,, ava ,.! "
stri = stri.replace(",", "").replace(".","").replace("!","")
stri = stri.strip()
print(stri)


