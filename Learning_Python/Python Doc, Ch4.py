#Pushing to github: git push origin main





# If statements, nonensical stuff for real hahhaahhaa.

val  = 0 # int(input("Enter an integer")) # prommpt a user to enter an int value 
if val < 0:
    val = 0
    print("Negative: we changed it to zero")
elif val == 0:
    print("value is equal to 0 good")
elif val == 1:
    print("val is equal to 1 hahahaha")
else:
    print("moore value good man sir")





#Time to learn for loops, goated loops FR

wordList = ['car', 'yomama', 'holaista', 'pupisto', 'holala']
for i in wordList:
    print(i, len(i))    # ouputs the words, and its characters counts





#Collections: No idea what this is, but it sees interestting. 

users = {'Hans': 'inactive', 'Eleonore': 'active', 'Karl': 'active'}
    # it seems like a collections is a list with every value in the list having 
    # set of items of thier own or something of that regards.

# It seems like we are going through every value in the list and getting a coper of
# thier 'items' using - users.copy().items()
for user, status in users.copy().items(): 
    if status == 'inactive':
        del users[user]        # Delete the users from the lists

#Create a new collection, and only tranfer value that are acitve
active_users = {}
for user, status in users.items(): # we are modifying teh actual list and not a copy of it
    if status == 'active':
        active_users[user] = status # Tranfers the value and its item to the new list





# 'Range()' Function, I also have no idea as to what this does but lets learn!!!

for i in range(5):  # Print the v
    print(i)