
#### Q1.

sentence = "What a pleasant day"
print(sentence[7:])


#### Q2.

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in a_list:
    print(i**2)


#### Q3.

base_number = int(input("Enter the base number: "))
power_number = int(input("Enter the power: "))

result = 1
for i in range(power_number):
    result*=base_number

print(result)


#### Q4.

tuple = (23, 44, 56, 12, 51, 19, 16, 22, 40)
even_list = []

for i in tuple:
    if i%2==0:
        even_list.append(i)

print(even_list)


#### Q5. 

user_number = int(input("Enter a number to calculate its factorial: "))

factorial = 1

for i in range(1,user_number+1):
    factorial*=i

print(factorial)


#### Q6. 

blist = [1, 2, 3, 4,5, 0, 'hello', 9, True]

output = []

for i in blist:
    if type(i) == int:
        output.append("integer")
    elif type(i) == bool:
        output.append("boolean")
    elif type(i) == str:
        output.append("string")

print(output)


#### Q7. 

cube_list = []

for i in range(1,11):
    cube_list.append(i**3)

print(cube_list)


#### Q8.

clist = ['a', 'b', 'c', 'd', 'e', 'f']

my_dict = {}
idx = 0

for i in clist:
    my_dict[i] = idx
    idx+=1

print(my_dict)