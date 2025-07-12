#### ----------- Use of sum, max, min --------------

intList = [2,3,6,8,4,1]
print(intList)
print('Maximum:',max(intList))               #print maximum from the list
print('Minimum Value:',min(intList))      #print minimum from the list
print('Sum of all items:',sum(intList))     #add all elements of a list


#### ------------------- SORTING LISTS -------------------

'''
sort() function changes the original list
'''

intList = [2,3,6,8,4,1]
intList.sort()
print(intList)
print(intList[0])

'''
for arranging in descending order
'''
intList = [2,3,6,8,4,1]
intList.sort(reverse = True)
print(intList)


#### -----------------------------------------------------------

'''
sorted() function will create a new list containing a sorted version of the list it is given.
'''

intList = [2,3,6,8,4,1]
newList = sorted(intList)
print(newList)

### descending order using sorted
newList = sorted(intList, reverse = True)
print(newList)


#### ------------------- REVERSE LIST -------------------

'''
reverse() function is used to reverse a sequence. It changes the original list.
'''

list_1 = ['apple', 'banana', 'mango', 'grapes']
print(list_1)

list_1.reverse()
print(list_1)
print(list_1[0])


#### ------------------------------------------------------

'''
reversed() function reverse a copy of original sequence and returns a reverse object.
'''

list_1 = ['apple', 'banana', 'mango', 'grapes']
print(reversed(list_1))
print(list(reversed(list_1)))

list_2 = list(reversed(list_1))
print(list_2)

print(list_1)


#### --------------------- NESTED LISTS --------------------

alist = [2,4,6,8]
blist = [1,3,5,7]
resultList = [alist, blist]
print(resultList)

print(resultList[0])
print(resultList[0][0])
print(resultList[1][2])

cList = [5,6,7]
resultList.insert(1,cList)
print(resultList)



#--------------------- ENUMERATE FUNCTION -----------------------

li = ['a','b','c','d','e']
print(enumerate(li))     # returns an object that needs to be converted into a list           
print(list(enumerate(li)))

'''
to iterate over a list using enumerate function
'''
newList = ['rose','sunflower','lily']

for index,element in enumerate(newList):
   print(index,element)