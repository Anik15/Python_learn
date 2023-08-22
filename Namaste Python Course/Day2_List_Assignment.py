# 1- write a program which takes single input from user containing first name,last name and age as comma separated value
# and display then in 3 lines in given format below.
# example user input : Ankit,Bansal,35
# output:
# First name is Ankit
# last name is Bansal
# Ankit is 35 years old
# note : do not hardcode name at any place

details = str(input("Please provide first and last name and age in comma separated format: "))
details_list = details.split(',')
f_name = details_list[0]
l_name = details_list[1]
age = details_list[2]
print(f'First name is {f_name}')
print(f'Last name is {l_name}')
print(f'{f_name} is {age} years old.')

# 2 - combined the 2 list and display the same without using extend method
list1= [1,3,4]
list2= [2,4,6]
list3= list1+list2
print(list3)

# 3- given a list list1=[1,2,3,4,5,6,7,8]
# display a new list which contains only odd position index values from above list.
mylist = [1,2,3,4,5,6,7,8]
newlist = mylist[1::2]
print(newlist)

# 4- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a ipl team name as input from user and display a list of all elements from that name.
# example : input : KKR
# output : ['KKR','LSG','PBKS']

ipl = ['CSK','MI','KKR','LSG','PBKS']
inpt = str(input("Enter a Team Name:"))
idx = ipl.index(inpt)
print(ipl[idx:])

# 5- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a ipl team name as input from user and display a list of all elements except input one
# example : input : KKR
# output : ['CSK','MI','LSG','PBKS']

ipl = ['CSK','MI','KKR','LSG','PBKS']
inpt = str(input("Enter a Team Name:"))
iplNew = ipl.copy()
iplNew.pop(ipl.index(inpt))
print(iplNew)

# 6- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma seprated values index,new_team .
# replace the index element of list with new value and display the same

# example : input : 2,SRH
# output : ['CSK','MI','SRH','LSG','PBKS']

ipl= ['CSK','MI','KKR','LSG','PBKS']
inpt = input("PLease Enter Index and New Team name(Comma seperated): ")
inptList = list(inpt.split(','))

idx = int(inptList[0])
team_name = inptList[1]

ipl.insert(idx,team_name)
print(ipl)



# 7 - ipl= ['CSK','MI','KKR','LSG','PBKS']
# take ipl team name as user input. display True if the team exists else display False.
ipl = ['CSK','MI','KKR','LSG','PBKS']
team_name = input("Enter a Team name that you want to search: ")

teamExist = team_name in ipl
print(teamExist)

# for i in ipl:
#     if i==team_name:
#         print('True')
#         break
#     else:
#         print('False')



# 8-ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma seprated values index,new_team . Add the new value at that index in the list.
# Display the old list , new list,length of original and new list
#
# example : input : 2,SRH
# output :
# old list : ['CSK','MI','KKR','LSG','PBKS'] and length 5
# new list : ['CSK','MI','SRH','KKR',LSG','PBKS'] and length 6

ipl= ['CSK','MI','KKR','LSG','PBKS']
team = input("Please Enter The Index and Team name (In comma separated): ")
teamList = team.split(',')
iplNew = ipl.copy()
idx = int(teamList[0])
team_name = teamList[1]
iplNew.insert(idx,team_name)
print(f'Old List : {ipl} and length {len(ipl)}')
print(f'New List : {iplNew}, and length {len(iplNew)}')
