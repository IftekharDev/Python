
####------------- Regex functions-------------------

import re

# matched_result = re.search("sun", "The sun is up")
# print(matched_result)

## Print the match
# print("Match :", matched_result.group())
 
###start and ending index of the match
# print("Span :", matched_result.span())
 
## Print starting index of the match
# print("Match :", matched_result.start())
 
## Print the ending index of the match
# print("Match :", matched_result.end())


#### ------------------match()--------------------------------------

'''
The match() function in regex checks if the pattern matches at the beginning of a string, 
returns a match object if successful or 'None' if not.
'''

# string = "The sun is up"

# matched_result_1 = re.match("sun", string)
# print(matched_result_1)

# string = "Sun is up"

# matched_result_2 = re.match("Sun", string)
# print(matched_result_2)


#### ----------------- Finditer --------------------

# aString = "The dog ran in a random way"
# match = re.finditer("ran", aString)
# print(list(match))
# print(type(match))

# for i in match:
#    print(i)
#    print("Span:",i.span())   
#    print("Start Index:",i.start())
#    print("End Index:",i.end())
#    print()

