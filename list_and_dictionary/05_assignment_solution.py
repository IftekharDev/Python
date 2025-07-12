
### Q1.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + " " + first_name)


### Q2.

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
print(num_1 + num_2)


### Q3.

list_1 = [2,4,6,8,9,3,5,8,9,1,5,9,3,7,2,3,9]
print(list_1.count(9))


### Q4.

animal_1 = ['Cat', 'Tiger', 'Kangaroo', 'Elephant']
animal_2 = ["camel", "rabbit", "lion","zebra"]
animal_1.extend(animal_2)
print(animal_1)


### Q5.

list_2 = ['truck', 'bicycle', 'rickshaw', 'car', 'motorbike']
print(list_2.index("car"))


### Q6.

list_3 = ['H', 'A', 'P', 'P', 'I', 'N', 'E', 'S', 'S']
string = ''.join(list_3)
print(string)


### Q7.

num = int(input("Enter a number: "))

if num%2 == 0:
    print(f"{num} is a even number.")
else:
    print(f"{num} is an odd number.")


### Q8.

scorecard_dict = {
    'student_1' : {
        "name" : "John",
        "score": 74
    },
    "student_2" : {
        "name" : "Atif Aslam",
        "score": 99
    },
    "student_3" : {
        "name" : "Arijit Singh",
        "score": 98
    }
}

scorecard_dict["student_2"]["score"] = 100
print(scorecard_dict)


### Q9.

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
operator = input("Choose the operator:")

if operator == "-":
    print(f'{num_1} {operator} {num_2} = {num_1 - num_2}')
elif operator == '*':
    print(f'{num_1} {operator} {num_2} = {num_1 * num_2}')
elif operator == '/':
    print(f'{num_1} {operator} {num_2} = {num_1 / num_2}')
else:
    print("Invalid operator")


## Q10.

first_name = input("Enter your first name: ")
last_name = input("Enter your second name: ")
full_name = first_name + " " + last_name

print(f"Your name is {full_name} and the length of your name is {len(first_name) + len(last_name)}")