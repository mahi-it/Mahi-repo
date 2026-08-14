print("welcome to the Interactive Personal Data Collector !")

name=input("\n Please enter your name : ")
age=int(input("Please enter your age :"))
height=float(input("Please enter your height in meter :"))
fav_number=int(input("Please enter your favourite number :"))

print("\n Thank you! Here is the Information we collected")

print("\n name :", name  , "(type :", type(name),", Memory Address : ", id(name),")") 
print("age :", age  , "(type :", type(age),", Memory Address: ", id(age),")") 
print("height :", height  , "(type :", type(height),", Memory Address: ", id(height),")") 
print("fav_number :", fav_number , "(type :", type(fav_number),", Memory Address : ", id(fav_number),")") 
 
curr_year = int(input("\n enter curr_year : "))
birth = curr_year - age

print("\n Your Birth  year is appoximately : ", birth ,"(based on your age of",age ,")")


print("\n Thank you for using the Personal Data Collector , Goodbye ! ")
 