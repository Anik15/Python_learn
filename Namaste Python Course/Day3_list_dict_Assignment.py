# 1- given a list of numbers, write a program to find the mean of the numbers in list
mylist = [1,2,3,4,5,6,7,8,9,10]
sum = sum(mylist)
mylistMean = sum/len(mylist)
print('Mean: ', mylistMean)

# 2- given a list of numbers unsorted, write a program to find the median of the numbers in list
list1 =[9,7,3,5,4,6,8,2,1,8]
list1.sort()
listLen= len(list1)
if listLen%2==0:
    med = (list1[listLen//2-1]+list1[listLen//2])/2
else:
    med = list1[listLen//2]
print(med)

# 3- from a list of numbers create 2 list , one containing only the even numbers and other only the odd numbers
myNum = [1,3,2,6,4,5,8,7,9]
myEvenNum = []
myOddNum = []
for i in myNum:
    if i%2==0:
        myEvenNum.append(i)
    else:
        myOddNum.append(i)
print('Odd List: ',myOddNum)
print('Even List: ',myEvenNum)

# 4- create a dictionary to store following attributes of CSK
# key "CSK" ; attributes : team full name , captain , playing 11 for each match(name of players),
# oppenont name (assume there are 3 matches only against MI, RCB , GT ) and result won/loss
d={'CSK':
       {
           'teamFullName':'Chennai Super Kings',
           'captain':'MSD',
           'playing11':['MSD','Jadeja','Rahane','Dube'],
           'opponent':['MI','RCB','GT'],
           'win':3,
           'loss':0
       }
}

# 5- in the previous dictonary add one more item for RCB. you can choose any 3 opponents.
d={'CSK':
       {
           'teamFullName':'Chennai Super Kings',
           'captain':'MSD',
           'playing11':['MSD','Jadeja','Rahane','Dube'],
           'opponent':['MI','RCB','GT'],
           'win':3,
           'loss':0
       },
    'RCB':
       {
           'teamFullName':'Royal Challengers Bangalore',
           'captain':'Du Plessi',
           'playing11':['Du Plessi','Kohli','Siraj','Maxwell'],
           'opponent':['MI','CSK','GT'],
           'win':0,
           'loss':3
       }
}
# print(d.keys())
# 6- write a program to take a positive number as input from user.
# if the user enters negative number then keep promting him to enter positive number until he enters the positive number
# and then print the same

num = int(input('Enter a Number: '))
while num<=0:
    print('Please Try Again!! Enter a Positive Number!')
    num = int(input('Enter a Number: '))
print(num)

# 7- consider the below list of list conatins following information :
#     # 1. The name of a university
#     # 2. The total number of enrolled students
#     # 3. The annual tuition fees

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]
#
# write a program to print follwoing information :
# 1- a list of all the universitites  : ['California Institute of Technology','Harvard',..so on]
# 2- total number of student entrolled in all the unversities together
# 3- mean of tuition fees

universityName = []
studentCount = 0

fees = []
for i in universities:
    universityName.append(i[0])
    studentCount = studentCount+i[1]
    fees.append(i[2])
print(studentCount)

avgFees = sum(fees) / len(universities)

print('University Name: ',universityName)
print('Total Students:', studentCount)
print('Mean Fees: ', avgFees)


# 8- write a program to convert above universities list to a dictionary. the keys should be the name of the university
universityDict = {}

for i in universities:
    keyName = i[0]
    universityValue = {'studentCount': i[1],'courseFees': i[2]}
    universityDict[keyName] = universityValue
print(universityDict)

# 9-  write a program that reverses a given string. For example, if the input is "Hello" from user, the output should be "olleH"
mystring1 = 'Hello'
print(mystring1[::-1])
sLen = len(mystring1)


# 10- write a program that finds the largest number in a list(unsorted) of integers without using sort/sorted method.
