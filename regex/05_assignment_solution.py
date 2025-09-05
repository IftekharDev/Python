
import re

### Q1.

phone_numbers = "0755-4926545  0765-3223345 3653-7497986 975423763"
phone_number_match = re.findall(r"\d{4}-(\d{7})", phone_numbers)
print(phone_number_match)


### Q2.

string = "I tried Hyderabadi Biryani and it was good, I'm for real it was good"
pattern_match = re.search(r"it was good", string)
print("Start Index = ", pattern_match.start())
print("End Index = ", pattern_match.end())


### Q3.

id_number = input("Enter your ID number: ")
id_format = r"INV\d{4}"
is_valid = re.match(id_format, id_number)
if is_valid:
    print(is_valid.group())
else:
    print("Invalid Id number")


### Q4.
##a.

text = "He's farmer. The farmers are the reason we eat. Farmers should be given respect"
farmer_obj = re.compile(r"farmers?", re.IGNORECASE)
search_results = re.findall(farmer_obj, text)
print(search_results)

##b.

farmer_obj = re.compile(r"farmers?")
search_results = re.findall(farmer_obj, text)
print(search_results)


### Q5.
text = "At the very beginning of the string, if the very first character is a word character."
search_text = input("Enter the text to search it: ")

matches = re.finditer(search_text, text)

for word in matches:
    print(word.start())


### Q6.

text = input("Enter a text to check: ")

start_with_number = re.compile(r"\b[\d].*")
end_with_number = re.compile(r".*[\d]\b")
start_end_with_number = re.compile(r"\b[\d].*[\d]\b")

if re.match(start_end_with_number, text):
    print("It starts as well as ends with a number.")
elif re.match(start_with_number, text):
    print("The text starts with a number.")
elif re.match(end_with_number, text):
    print("It ends with a number")
else:
    print("Unrecognizable pattern")


### Q7.

##(a)

with open('Text.txt','r') as var:
   texts = var.read()

new_texts = re.sub(r'[^a-zA-Z0-9\n\s]+','',texts)

with open('Text.txt','w') as wri:
   texts = wri.write(new_texts)

print('Program Executed')


##(b)

with open('Text.txt', 'r') as var:
   texts = var.read()

new_texts = re.sub(r'\n',' ',texts)
with open('Text.txt','w') as wri:
   texts = wri.write(new_texts)

print('Program Executed')


##(c)

with open('Text.txt', 'r') as var:
   texts = var.read()

new_texts = re.sub(r'\b\w{1,2}\b','',texts)
with open('Sal.txt','w') as wri:
   texts = wri.write(new_texts)

print('Program Executed')


##(d)

with open('Text.txt', 'r') as var:
   texts = var.read()

new_Texts = re.sub(r'[\w\._%+-]{1,20}@[\w]{1,10}\.[\w]{1,10}','EmailID',texts)
with open('Sal.txt','w') as wri:
   texts = wri.write(new_Texts)

print('Program Executed')