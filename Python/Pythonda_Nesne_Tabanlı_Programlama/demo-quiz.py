#Question class

class Question:
    def __init__(self,text,choices,answer):
        self.text= text
        self.choices= choices
        self.answer= answer

    def checkAnswer(self,answer):
        return self.answer == answer #self.answer kendi cevabımız answer dışarıdan gelen cevap

    
"""        
q1=Question("En iyi programlama dili hangisidir?",["C#","Python","Javascript","Java"],"Python")
q2=Question("En popüler programlama dili hangisidir?",["Java","C#","Javascript","Python"],"Python")
q3=Question("En çok kazandıran programlama dili hangisidir?",["Java","Javascript","Python","C#"],"Python")

print(q1.checkAnswer("Python")) True
print(q1.checkAnswer("C#")) False

"""
#Quiz class
class Quiz:
    def __init__(self,questions):
        self.questions =questions
        self.score= 0
        self.questionIndex= 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question=self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in  question.choices:
            print("-"+q)
        answer=input("Cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question=self.getQuestion()

        if question.checkAnswer(answer):
            self.score +=1
            self.questionIndex +=1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()

    def showScore(self):
        print("Score: "+self.score)  
        
q1=Question("En iyi programlama dili hangisidir?",["C#","Python","Javascript","Java"],"Python")
q2=Question("En popüler programlama dili hangisidir?",["Java","C#","Javascript","Python"],"Python")
q3=Question("En çok kazandıran programlama dili hangisidir?",["Java","Javascript","Python","C#"],"Python")
questions=[q1,q2,q3]

quiz=Quiz(questions)
questions=quiz.getQuestion()
print(questions.text)

quiz.displayQuestion()















