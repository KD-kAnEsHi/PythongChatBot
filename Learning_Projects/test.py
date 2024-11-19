


#There is no possible call that will make it return True as the keyword 'name' will always bind to the first parameter. For example:



def getQuestionsandAnswer(quesAnsDictionar):
    quesAnsDictionar["Fruid"] = "apple"




quesAnsDictionar = {}
print(getQuestionsandAnswer(quesAnsDictionar))
print(quesAnsDictionar)