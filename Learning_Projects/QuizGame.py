# The purpose of this project it to build something using all the python knowledge i have gained
#by going through  Ch1 - Ch4 of pythons documentations.


# Project Description:
# In this project, you will create a quiz game where the user is asked multiple-choice questions, and 
# they have to select the correct answer. The program will keep track of the user's score and display it 
# at the end of the quiz.


print()
print("------------------------------Welcome to Quiz game-----------------------------")
print()
print("Here is how the game works: ")
print("Input your questions and answer, I will shuffle and have you answer each question")
print()
print()




def getQuestionsandAnswer(quesAnsDictionar):

    while(True):
            
        print ("Please enter the Question: ")
        questionInput = input()
        quesAnsDictionar[questionInput] = []

        print("Please enter 4 answers: ")
        for i in range(4):
            quesAnsDictionar[questionInput].append(input())
            print()

        print ("please enter the index of correct answer: ")
        corAnswer = input()

        print("Would you like to enter more questions, Y / N")
        more = input()

        if(more == "N"):
            return False


def main():

    quesAnsDictionar = {}

    newDict = getQuestionsandAnswer(quesAnsDictionar)

    print(newDict)


