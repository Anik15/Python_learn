# 1- create a txt file and put 4-5 lines.
# Now create another file from the previous file and at the end of each line put the count of words.

# example :
# file 1:
# this is namaste sql course
# this is python course
# this assignment is part of day4 lecture

# file2:this is namaste sql course:5
# this is python course:4
# this assignment is part of day4 lecture:7

# f = open('test.txt', 'r')
# # print(f.read())
#
# for line in f:
#     print(line)








# 2- given below dictonaries of states and their capital:

# capitals_dict = {
# 'Alabama': 'Montgomery',
# 'Alaska': 'Juneau',
# 'Arizona': 'Phoenix',
# 'Arkansas': 'Little Rock',
# 'California': 'Sacramento',
# 'Colorado': 'Denver',
# 'Connecticut': 'Hartford',
# 'Delaware': 'Dover',
# 'Florida': 'Tallahassee',
# 'Georgia': 'Atlanta',
# }

# pick a state from above dictonary and ask user to enter the capital of the state.
# If the user answers incorrectly, then repeatedly ask them for the capital until they either enter the correct answer or type "exit".
# If the user answers correctly, then display "Correct" and end the program. However, if the user exits without guessing correctly,
# display the correct answer and the word "Goodbye".

# Note: Make sure the user isn’t punished for case sensitivity. In other words, a guess of "Denver" is the same as "denver".
# Do the same for exiting—"EXIT" and "Exit" should work the same as "exit".



# 3- write a program to take state as input from user and print the capital of the state using above dictonary.
# If the state is not there in dictonary then print "sorry , information not available"




# 4- Let say You have one 100 cats.
# One day, you decide to arrange all your cats in a giant circle. Initially,none of your cats has a hat on.
# You walk around the circle a 100 times, always starting with the first cat (cat #1).
# Each time you stop at a cat, you check if it has a hat on. If it doesn’t, then you put a hat on it.
# If it does, then you take the hat off.



# 1. The first round, you stop at every cat, placing a hat on each one.
# 2. The second round, you stop only at every second cat (#2, #4, #6, #8, and so on).
# 3. The third round, you stop only at every third cat (#3, #6, #9, #12, and so on).
# 4. You continue this process until you’ve made one hundred rounds
# around the cats. On the last round, you stop only at cat #100.

# Write a program that simply outputs which cats have hats at the end.
