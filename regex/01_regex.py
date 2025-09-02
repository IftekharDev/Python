
#### ------------------ REGULAR EXPRESSIONS ------------------

'''
Regular Expressions allows us to search for a specific pattern
Regular expressions allows us to-
1. Search for a specific string in a large amount of data
2. Verify that a string has the proper format (Email, Phone)
3. Find a string and replace it with another string
4. Format data into the proper form 
'''

import re

# animalstr = 'cat rat mat bat cat sat Mat Cat pat hat fat'

### search returns first occurance of match object
# print(re.search('cat', animalstr))


### findall returns list of matches
# print(re.findall('cat',animalstr))


###[] accepts only one character
# print(re.findall('[cC]at', animalstr))


### Use ^ to denote any character except whatever characters are between the brackets
# print(re.findall('[^bsmM]at', animalstr))


### printing a range of matches
# string = re.findall('[c-m]at',animalstr)
# print(string)


#### -------------- Replace All Matches --------------

'''
You can compile a regex into pattern objects which provide additional methods
sub() replaces items that match the regex in the string
'''


# string1 = 'earth revolves around the sun'
# n = re.compile('earth')

# finalStr = re.sub(n, 'moon', string1)

### substituting regex pattern in a string
# print(finalStr)


### Another way of substituting

# a = re.compile('earth')
# match = a.sub('Saturn', string1)
# print(match)


# string1 = 'earth revolves round the sun'
# match = re.sub('earth', 'Saturn', string1)
# print(match)


# text = "The quick brown fox jumps over the lazy dog. The fox is fast."
# pattern = r"fox"
# replacement = "cat"

### Replace only the first occurrence by setting count=1
# new_text_one_replacement = re.sub(pattern, replacement, text, count=1)

# print(new_text_one_replacement)


#### ---------- Solving Backslash Problems ----------
 
'''
Regex use the backslash to designate special characters and Python does the same inside strings which causes issues
'''

# print("\\stuff")

# string = "Here is \\stuff"

# searched_result = re.search("\\stuff", string)
# print(searched_result)

# searched_result = re.search("\\\\stuff", string)
# print(searched_result)

# searched_result = re.search(r"\\stuff", string)         # using raw string
# print(searched_result)


#### ---------- Matching Any Character ----------
'''
. matches any character, but what if we want to match a full stop. Backslash the full stop
'''

# randStr = "F.B.I. I.R.S. CIA Dr. Mr."

# search = re.search(".",randStr)
# print(search)

# print("Matches :",re.findall(".\..\..\.", randStr))       ##It gives warning for invalid escape sequence


### The 'r' before the string makes it a raw string
# print("Matches :", re.findall(r".\..\..\.", randStr))


### Use '\\' to create a literal backslash in a normal string
# print("Matches :", re.findall(".\\..\\..\\.", randStr))


#### ---------- Matching Whitespace ----------
 
# randStr = """This is a long
# string that goes
# on for many lines"""

# print(randStr)

# # Remove newlines
# match = re.sub("\n", " ", randStr)
# print(match)