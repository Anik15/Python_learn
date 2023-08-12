# 1- write a program which takes 2 inputs from the user : weight(kg) and height(meter) and prints the BMI in the output.
# BMI = weight / (square of height)
import math as m
weight = float(input("Please Enter your Weight(kg): "))
height = float(input("Please Enter your Height(meter): "))
bmi = round(weight/m.pow(height,2),2)
print("Your BMI is: ",bmi)

# 2- write a program which takes the name of the user as input and
# replace all the occurence of character 'a' in the name to 'b' and print it.
name=str(input("Please Enter your name: "))
name = name.lower().replace('a','b')
print("Replaced Name: ",name)

# 3- write a program which takes 2 inputs from user as principle amount (int) and rate of annual interest (float) and
# print the expected total amount  after  2 years.
p = int(input("Please Enter the principal Amount: "))
r = float(input("Please Enter the Interest: "))
si = p+(p*r*2/100)
print("Return in simple interest: ",si)
ci = p*pow((1 + r/100),2)
print("Return in compound interest: ",ci)

# 4- write a program which takes city name from user input. irrespective of in which case user enters the city name,
# print the city name in camel case meaning first letter should be capital and rest in small.
# example : input : MYSORE ,  print - > Mysore
city = str(input("Please Enter the city: "))
city = city.capitalize()
print("City name in Camel Case: ",city)

# 5- write a program which takes the name of the user as input and
# print the index of character 'a' in the string. if 'a' is not there then return -1.
name = input("Enter your name: ")
index = name.lower().find('a')
print("Index of 'a':" + str(index))

# 6-  Display the number of letters in the below string
my_word = "antidisestablishmentarianism"
print("Length of my word: ",len(my_word))

# 7- take 3 inputs from user : first name , last name and age . Display the information in below format
# exmaple
# first name : MOhit
# last name : sharma
# age 32
# Display : my name is Mohit Sharma and I am 32 years old.
# note that first letter of first name and last name both should be in capital letters and rest in small.

first_name = str(input("Please Enter your First Name: "))
last_name = str(input("Please Enter your Last Name: "))
fc_name = first_name.capitalize()
lc_name = last_name.capitalize()
age =int(input("Please Enter your age: "))
print(f"My name is {fc_name} {lc_name} and I am {age} years old.")

# 8-take 3 inputs from user : first name , last name and company name.
# create the email alias for the user and display it.
# Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
# example
# first name : MOhit
# last name : sharma
# company : infosys
# Display : morma@infosys.com
# note full email id should -be in lower case

first_name = str(input("Please Enter your First Name: "))
last_name = str(input("Please Enter your Last Name: "))
company = str(input("Please Enter your Company Name: "))

email = first_name[:2].lower()+last_name[-3:].lower()+'@'+company.lower()+'.com'
print("Your Email Id: ",email)

email2 = f"{first_name[:2].lower()}{last_name[-3:].lower()}@{company.lower()}.com"
print(email2)
