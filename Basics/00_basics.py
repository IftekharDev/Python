
#### -----------Output function----------

print("Hello World")

'''
comments are identified by a # symbol
comments are written by a programmer to write his thought process while writing the code
'''


#### ------------- Indentation ---------------
'''
It refers to adding whitespaces at the beginning of a statement.
'''


###-----------------------------------------------------------------


####  -------end-------
'''
end = "" is used to add two strings and print them on a single line
'''

print("Hello World", end=" ")
print("it's a Lovely day !")


### ---------------------------------------------------------------


#### --------------  Escape Sequence Characters ----------------

### An escape character is a backslash '\' followed by any character needed to insert

'''
\n - newline character
\t - tab
\' - single quote
\" - double quotes
\\ - backslash
'''

print('Hello \nWorld')
print('Hello\tWorld')
print('Father\'s name')
print("\"All\'s well that ends well\"")
print('This inserts a backslash\\ in a string')



### Qs. Print the following
'''
Twinkle, twinkle, little star,
	How I wonder what you are!
    		Up above the world so high,
            Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are!
'''


print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond\
in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!")



### ---------------------------------------------------------------


#### -------------- Raw String ------------------

'''
Raw string are used to write something as it is.
It doesn't escape any character and treats single backslash as literal character.
'''

print(r'Hello \nWorld')
print(r'hello\tWorld')
print(r'"\"All\'s well that ends well\""')


### ---------------------------------------------------------------


####   -------   input() Function  ---------------------
'''
In Python, you can take input from the user using the input() function.
'''

userInput = input('enter something:' )
print(userInput)

name = input('Enter your name: ')
print('Hello' ,name)


### ---------------------------------------------------------------


#### ----------   type() Function  ----------------
'''
In Python, The type() function is used to check the type of an object.
'''

a = 'orange'
print(type(a))

b = '12'
print(type(b))

c = 3
print(type(c))

d = 3.2
print(type(d))

e = 'true'
print(type(e))

f = True
print(type(f))


### ---------------------------------------------------------------


#### ------------------  Format() Method --------------------
'''
In Python, the format() method is used to create formatted strings.
It helps you build strings where you can insert values or variables in specific positions within the string.
'''

name = 'xyz'
Hobby = 'Programming'
print('My Name is {}, My Hobby is {}.'.format(name,Hobby))

userName = input('enter your name: ')
age = input('enter your age: ')
print('My name is {}, I am {} years old.'.format(userName,age))


### ---------------------------------------------------------------


#### ---------- formatted string ----------------


name = input("Enter your name: ")
Hobby = input("Tell us your hobby: ")
print(f'My Name is {name}, My Hobby is {Hobby}.')

userName = input("Enter your Username: ")
age = input("Enter your age: ")
print(f'I am {userName} and i am {age} years old.')



###---------------------------------------------------------------

####     Practice

name = "xyz"
age = 25

print(name)
print(age)


name_1 = input("Please enter your name: ")
age_1 = input("Please enter your age: ")

print("Your name is",name_1, "and your age is", age_1)
print("Your name is {} and your age is {}".format(name_1, age_1))
print(f"Your name is {name_1} and your age is {age_1}")


name = "hjhjkhhj"
print(len(name))