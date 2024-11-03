#Pushing to github: git push origin main



# Exponents: 
square = -2 ** -2 + 2 ** 4 # Such a simple way of squaring integers :) : 2 * 2 * 2 * 2 = 16.


# concatnation in Python
string0 = "Good morning sir"
string1 = "The wind blow southwest mr.so"
string2 = "The wind sure does blow from not only south by also west"

string3 = "Hey papa how come you work everyday and you cant feed me still?"
numstostring = 10
numsBeforeString = 9
#print(string1, string2)


#Python: Lists
squareList = [1, 2, 4, 10, 16, 25]
squareList[3] = 9
squareList.append(6**2)
squareList.append(7**2)
print(squareList)

squareList[0:2] = ['A', 'B', 'C']
print("newList" + str(squareList))
print(len(squareList))

square = squareList # copy the element into the new list
id(square) == id(squareList) # creates another list that has reference to the originals
# square list so any changes made to the new list will be seen in the old list as well


squareList[:]  # Clears the list by replacing all the elemt with an empty list
print(squareList[4:5])  # print value in array from index 3 to 5
squareList[4:5] = [] # removes the values in and inbetween these indexe


print(squareList([-1])) # Print in revers: print the last index in the list

i = 0
while i < len(squareList):
        print(squareList[i])
        i += 1