# The purpose of this project it to build something using all the python knowledge i have gained
#by going through  Ch1 - Ch4 of pythons documentations.


# Project Description:
# In this project, you will create a quiz game where the user is asked multiple-choice questions, and 
# they have to select the correct answer. The program will keep track of the user's score and display it 
# at the end of the quiz.

import random 

print()
print("---------------------------------Welcome to Quiz game---------------------------------")
print()
print("Input your questions and answer, I will shuffle them and have you answer each questions")
print()
print()




def getQuestionsandAnswer(quesAnsDictionar):

    while(True):
            
        print ("Please enter the Question: ")
        questionInput = input()
        quesAnsDictionar[questionInput] = []            # what is an        {apple: [rock, pencils, phone, fruit], 3},
                                                                    #       {lion: [anime, pencils, phone, fruit], 0}
        print("Please enter 4 answers: ")
        for i in range(4):
            quesAnsDictionar[questionInput].append(input())
            print()

        print ("please enter the index [0-3] of correct answer: ")
        quesAnsDictionar["correctAns"] = input()

        print("Would you like to enter more questions, Y / N")
        more = input()

        if(more == "N", "n", "nope", "nah"):
            return 


def askQuiz(quesAnsDictionar):
    
    #quizList = quesAnsDictionar.items()
    score = 0

    print()
    for Key, val in quesAnsDictionar.items():
        print()
        print("Questions Number " + i)
        print(quizList())


    # print(random.choice(quizList))

    # return



def main():

    quesAnsDictionar = {}

    getQuestionsandAnswer(quesAnsDictionar)

    askQuize(quesAnsDictionar)

    print(quesAnsDictionar)

    #print("Would you like to take the quiz? Y/N")
    #if(input() == "Y"):
    #    outputQuestions(quesAnsDictionar)
    




main()
