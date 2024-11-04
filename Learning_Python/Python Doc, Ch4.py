#Pushing to github: git push origin main





print()
print()
print("Topic: If Statement")
# If statements,   nonensical stuff for real hahhaahhaa.

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





print()
print()
print("Topic: For Loops")
#Time to learn for loops, goated loops FR

wordList = ['car', 'yomama', 'holaista', 'pupisto', 'holala']
for i in wordList:
    print(i, len(i))    # ouputs the words, and its characters counts





print()
print()
print("Topic: Collection")
#Collections: No idea what this is, but it sees interestting. 

users = {'Hans': 'inactive', 'Eleonore': 'active', 'Karl': 'active'}
    # it seems like a collections is a list with every value in the list having 
    # set of items of thier own or something of that regards.

# It seems like we are going through every value in the list and getting a coper of
# thier 'items' using - users.copy().items()
for user, status in users.copy().items(): 
    if status == 'inactive':
        del users[user]             # Delete the users from the lists

#Create a new collection, and only tranfer value that are acitve
active_users = {}
for user, status in users.items():   # we are modifying teh actual list and not a copy of it
    if status == 'active':
        active_users[user] = status  # Tranfers the value and its item to the new list





print()
print()
print("Topic: Range")
# 'Range()' Function, I also have no idea as to what this does but lets learn!!!

for i in range(5):          # Range generate an arithmetic progression of a number ex: 5: 0 1 2 3 4
    print(i)

#Range: Steps - specifying the increments of the range
list(range(5, 10))          # Creates a list and add the values between 5 to 10 in it
print()
list(range(0, 10, 2))       # Creates a lits and add the values between 0 to 10 in an increment of 2
print()
list(range(-10, -100, -30)) # Creata a lists and add the values between -10 to -100 in an increment of -30


words = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(words)):
    print(i, words[i])





print()
print()
print("Topic: Break and Conitnue")
# 'break' statemetn breaks out of the innermosts enclosing while loop and for loop
for out in range(2, 10):
    for inner in range(2, out):
        if out % inner == 0:
            print(" x is equal to n")
            break

# continue end the current iterations and skips to the next iteration of the loop
for num in range(2, 10):
    if num % 2 == 0:
        print("even numbers: continue")
        continue





print()
print()
print("Topic: Else statement for While/For Loops")
# We can have an else statement that execute after each iteration of the for/while loop running
# Does not work if the loop was terminated by a break, or return statement

for outter in range(2, 10):
    for innner in range(2, outter):
        if outter % inner == 0:
            print("outter: This is not a prime " + str(outter))
    else:
        print(outter, " is a prime number")





print()
print()
print("Topic: Pass Statements")
# Generally does nothing, can be used wehn a statement is requrie syntactycally

#while True:     # Will go on running forever until  
   # pass






print()
print()
print("Topic: Match/Switch Statement")
# A matarch statement that take an experssion an dcompre its value to sucessive 
# pattern a sone or more bloocks

def checkError(status):
    match status:
        case 201:
            return 'Its all oh ok' 
        case 404:
            return "Not Found" 
        case 418:
            return "I am a tea pot"
        case _: # defaul statement
            return "Hey memo, check internet insted"      

# Check if the inserted points, fits compared ot my golves
match point:
    case(0, 0):
        print("Origine points")
    case(0, y):
        print(f"Y={y}")
    case(X, 0):
        print(f"Y={X}")
    case _:
        raise ValueError("Not a points: return to normal live")


print()
print("Match/Switch Statement -: If Clause/Guards")
# Add an 'if clause' to a pattern, also reffered as the guard. If the guard is false, match gos on to try the next
# case block. 






