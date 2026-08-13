# -*- coding: utf-8 -*-

#basic
print("hello")

name = input("enter your name :")
print("hello",name)

course ='data sci'
print(course)
course=' sci'
print(course)
course='data '
print(course)

#Arithematic Operation
a=100
b=200

a+b

a-b
#multiplication
a*b

a/b

a%b

a**2

132//10

#Comparison Operation
a==b

a!=b

a>b

a<b

a>=b

a<=b

#Assign Opeartion
a=b

print(a)

a+=2

print(a)

a-=4
print(a)

a*=4
print(a)

a/=4
print(a)

a%=5
print(a)

a=100
a//=11
print(a)

a**=2
print(a)
#logical Operation
a = 0
not(a)

# Identity Operator
a=100
b=500
a is  b

#Membership Operator
a=[1,2,3,4,5,6]
1  not in a

(a:= b)
print(a)

if(name:=input("enter name :"))== "mahi":
   print("hello",name)

#type of variable
a=100

id(a)

type(a)

#String Functions
l="    pyhton  java    "

l.strip()

l="   mahi here  "

l.lower()

l.upper()

l.strip()

l.split(" ")

l.find("mahi")

l.replace("mahi","world")

a="mahi patel"

a.title()

a.capitalize()

a={123,"mahi"}

type(a)

name="mahi"
age=20
f_string="my name is %s and my age is %d" %(name,age)
print(f_string)

name="mahi"
age=20
f_string="my name is {} and my age is {}" .format(name,age)
print(f_string)

name="mahi"
age=20
f_string= f"my name is {name} and my age is {age}"
print(f_string)

a=("10","20","30","40")
a[1].replace("20","50")

# Dictionary 
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(my_dict["name"])
print(my_dict["age"])





my_dict["email"] = "mahi@example.com"


my_dict["age"] = 20

del my_dict["city"]

print(my_dict)

print(my_dict.keys())

print(my_dict.values())

print(my_dict.items())

print(my_dict.get("age"))
print(my_dict.get("phone", "Not Found"))

new_data = {"city": "Los Angeles", "country": "USA"}
my_dict.update(new_data)

print(my_dict)

removed_value = my_dict.pop("age")
print(removed_value)

last_item = my_dict.popitem()
print(last_item)

print(my_dict.setdefault("gender", "Female"))
# If 'gender' does not exist, it gets added
print(my_dict)

my_dict.clear()
print(my_dict)

original = {"a": 1, "b": 2}
copy_dict = original.copy()

copy_dict["b"] = 10
print(original)  # Output: {'a': 1, 'b': 2}
print(copy_dict)

squares = {x: x**2 for x in range(1, 6)}
print(squares)

my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

a =my_dict["name"]
b =my_dict["age"]

print(a)

a=10

b=str(a)
print(b)

type(b)



