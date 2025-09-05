
#### ---------------Metacharacters and special sequence characters------------------

import re

r'''
[ ]   : Match what is in the brackets
[^ ]  : Match anything not in the brackets
( )   : Return surrounded submatch
.     : Match any 1 character or space
+     : Match 1 or more of what proceeds (quantifier)
?     : Match 0 or 1 (quantifier)
*     : Match 0 or More (quantifier)
*?    : Lazy match the smallest match (quantifier)
\b    : Word boundary
^     : Beginning of String
$     : End of String
\n    : Newline
\d    : Any 1 number
\D    : Anything except a number
\w    : Same as [a-zA-Z0-9_]
\W    : Same as [^a-zA-Z0-9_]
\s    : Returns a match where the string contains a white space character
\S    : Returns a match where the string DOES NOT contain a white space character
{5}   : Match 5 of what preceeds the curly brackets
{5,7} : Match values that are between 5 and 7 in length
'''


#### -------------- MATCHING A SINGLE SEARCH --------------

# phone = "567-3746-3767"
# print(re.search(r"\d{3}-\d{4}-\d{4}", phone))

# name = "John Doe"
# n = re.findall(r"\w{4}\s\w{3}", name)
# print(n)

# x = "I got 90 marks in maths"
# print(re.findall(r"\D{1,30}",x))

# print(re.findall(r"\D+", "Hello 123"))


#### -------------- MATCHING MULTIPLE SEARCHES --------------

# numStr = "123 12345 123456 1234567 12345678 123456789"
# print(re.findall(r"\d{5,7}", numStr))
# print(re.findall(r"\b\d{5,7}\b", numStr))


# PhoneNum = "0755-2345192 0755-5690432 075-5647381"
# matches = re.findall(r"\d{4}-\d{7}", PhoneNum)
# print(matches)


### Check if it is a phone number
# phNum = "412-555-1212"

# if re.search(r"\w{3}-\w{3}-\w{4}", phNum):
#    print("It is a phone number")
# else:
#    print("Invalid")


#### ---------------- EMAIL PATTERN SEARCH ----------------

# email = """@grow_526gmail.com
# 5543_tr.@yahoo.com
# limit.less@hotmail.com"""

# mail = re.findall(r"[\w\._%+-]{1,20}@[\w]{1,10}\.[\w]{1,10}", email)
# print(mail)


#### -------------- MATCHING ZERO, ONE, MANY --------------

###zero or one (?)
# randstr = "cat cats Catsss catssssssssss"
# pattern = re.findall("[cC]ats?", randstr)
# print(pattern)

###one or many (+)
# match = re.findall("[cC]ats+", randstr)        
# print(match)

#zero or many (*)
# match =  re.findall("[cC]ats*", randstr)
# print("Matches :",match)