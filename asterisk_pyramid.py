my_list = [0, 1, 2, 3, 4]

for i in range(len(my_list)):
    print(" " * (len(my_list)-i-1) + "*" * (i+1) + "*" * i)

for i in range(len(my_list)):
    print(" " * my_list[-i-1] + "#" * (i+1) + "#" * i)

for i in range(5):
    #n-i-1 times
    for j in range(4-i):
        print(" ", end="")
    for k in range(i+1):
        print(".", end="")
    print("." * i)

for num in range(5):
    for i in range(0, num+1):
        print(i+1,end=" ")
    print("")

patient = {"name": "John Smith", "age" : 20, "is_new" : True}

if patient["is_new"]:
    print("Patient's Name:", patient["name"])
    print("Patient's Age:", patient["age"])
    print(f"{patient['name']} is our new patient")
else:
    print("Patient's Name:", patient["name"])
    print("Patient's Age:", patient["age"])
    print(f'{patient["name"]} is our old patient')

'''q = "What is your name? "
q1 = "What is your favourite color? "
name = input(q)
color = input(q1)
print(f"My name is {name} and my favourite color is {color}.")'''

'''weight = input('Enter weight in lbs: ')
to_kilo = 0.453592 * float(weight)
print(weight + " lbs in kg is: ", to_kilo)'''
#cannot concate float(to_kilo) with string

name = "Niloy Kumer Bhadra"
print(name[1:-1])

price = 1000000

is_credit = True

if is_credit:
    print("Down Payment:", price - price * 0.1)
else:
    print("Down Payment:", price - price * 0.2)

has_credit = True
has_criminal_rec = False

if has_credit and not has_criminal_rec:
    print("OK")

weight = float(input("Enter Your weight: "))
unit = input("Is it lbs(l) or kg(k)? ")

if unit.upper() == 'K':
    print(f"You are {weight*2.20} pounds")
elif unit.upper() == 'L':
    print(f"You are {weight*0.45} kilograms")
else:
    print("Bad units!")


