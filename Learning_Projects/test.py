


#There is no possible call that will make it return True as the keyword 'name' will always bind to the first parameter. For example:



def getQuestionsandAnswer(quesAnsDictionar):

        print ("Please enter the Question: ")
        questionInput = input()
        quesAnsDictionar[questionInput] = []

        print("Please enter 4 answers: ")
        for i in range(4):
            quesAnsDictionar[questionInput].append(input())
            print()

        print ("please enter the index of correct answer: ")
        corAnswer = input()


def main():

    quesAnsDictionar = {}

    getQuestionsandAnswer(quesAnsDictionar)

    #print(quesAnsDictionar)

