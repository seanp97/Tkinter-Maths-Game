from tkinter import *
import sys
import random

addBool = False
minusBool = False
divideBool = False
multiplyBool = False
questionNum = 0
tally = 0

def questionAns():
    try:
        questionNum = Entry.get(questionEnt)
        questionNum = float(questionNum)
        questionVal.configure(text="You will be asked a max number of " + str(questionNum))
        global result
        randNumsOne = random.randrange(1, questionNum / 2)
        randNumsTwo = random.randrange(1, questionNum / 2)
        result = 0
        if addBool:
            genMath.configure(text="What is " + str(randNumsOne) + " + " + str(randNumsTwo))
            result = randNumsOne + randNumsTwo
        elif minusBool:
            genMath.configure(text="What is " + str(randNumsOne) + " - " + str(randNumsTwo))
            result = randNumsOne - randNumsTwo
        elif divideBool:
            #genMath.configure(text="What is " + str(randNumsOne) + " ÷ " + str(randNumsTwo))
            #result = randNumsOne / randNumsTwo
            if randNumsOne == max(randNumsOne, randNumsTwo):
                genMath.configure(text="What is " + str(randNumsOne) + " ÷ " + str(randNumsTwo))
                result = randNumsOne / randNumsTwo
            else:
                genMath.configure(text="What is " + str(randNumsTwo) + " ÷ " + str(randNumsOne))
                result = randNumsTwo / randNumsOne
                
        if multiplyBool:
            genMath.configure(text="What is " + str(randNumsOne) + " x " + str(randNumsTwo))
            result = randNumsOne * randNumsTwo
            errorLabel.configure(text=" ")
            
        if addBool == False and minusBool == False and divideBool == False and multiplyBool == False:
            errorLabel.configure(text="Pick a maths operation first")
    except:
        errorLabel.configure(text="Pick an even number!!")
        questionEnt.delete(first=0, last=1000)
        Entry.insert(questionEnt, 0, "Enter an even number")
    
def AddQues():
    global addBool
    global minusBool
    global divideBool
    global multiplyBool
    addBool = True
    minusBool = False
    divideBool = False
    multiplyBool = False
    global tally
    tally = 0
    tallyLabel.configure(text="Score: " + str(0))
    emptyLab.configure(text="You chose Addition")
    
def MinusQues():
    global addBool
    global minusBool
    global divideBool
    global multiplyBool
    addBool = False
    minusBool = True
    divideBool = False
    multiplyBool = False
    global tally
    tally = 0
    tallyLabel.configure(text="Score: " + str(0))
    emptyLab.configure(text="You chose Subtraction")
    
def DivideQues():
    global addBool
    global minusBool
    global divideBool
    global multiplyBool
    addBool = False
    minusBool = False
    divideBool = True
    multiplyBool = False
    global tally
    tally = 0
    tallyLabel.configure(text="Score: " + str(0))
    emptyLab.configure(text="You chose Division")
    
def MultQues():
    global addBool
    global minusBool
    global divideBool
    global multiplyBool
    addBool = False
    minusBool = False
    divideBool = False
    multiplyBool = True 
    global tally
    tally = 0
    tallyLabel.configure(text="Score: " + str(0))
    emptyLab.configure(text="You chose Multiplication")
    
def questionCount():
    try:
        global questionCountVal
        questionCountVal = Entry.get(howManyQuestionsEnt)
        questionCountVal = int(questionCountVal)
        emptyLab.configure(text="You picked " + str(questionCountVal) +  " questions")
    except:
        howManyQuestionsEnt.delete(first=0, last=1000)
        Entry.insert(howManyQuestionsEnt, 0, "Enter a number")
    
def getUserAnswer():
    try:
        userAnswer = Entry.get(userAns)
        userAnswer = float(userAnswer)
        newUserAnswer = round(userAnswer, 2)
        global result
        if newUserAnswer == result:
            ansResult.configure(text="Correct!")
            questionAns()
            userAns.delete(first=0, last=9999)
            global tally
            tally += 1
            tallyLabel.configure(text="Score: " + str(tally))
            global questionCountVal
            
            if tally == questionCountVal:
                app.destroy()
        
        else:
            ansResult.configure(text="Incorrect! The answer was " + str(result))
            questionAns()
            userAns.delete(first=0, last=9999)
            tally -= 1
            tallyLabel.configure(text="Score: " + str(tally))
            
            if tally < 0:
                tallyLabel.configure(text="Score: " + str(0)) 
                tally = 0        
    except:
        userAns.delete(first=0, last=9999)
        Entry.insert(userAns, 0, "Enter a number")

app = Tk()
app.title("Helping With Maths")
app.geometry("1000x500")

operLabel = Label(app, text="What sort of maths questions would you like? Must be an even number", pady=20, padx=20)
operLabel.grid(column=1, row=0)

addBtn = Button(app, text="Addition", bd=3, command=AddQues)
addBtn.grid(column=1, row=1)
tallyLabel = Label(app, text="Score: " + str(0))
tallyLabel.grid(column=2, row=0)

minusBtn = Button(app, text="Subtraction", bd=3, command=MinusQues)
minusBtn.grid(column=1, row=2)

divideBtn = Button(app, text="Division", bd=3, command=DivideQues)
divideBtn.grid(column=1, row=3)

multiplyBtn = Button(app, text="Multiplication", bd=3, command=MultQues)
multiplyBtn.grid(column=1, row=4)

emptyLab = Label(app, text=" ", pady=20, padx=20)
emptyLab.grid(column=1, row=5)

howManyQuestionsLab = Label(app, text="How many question would you like?", pady=20, padx=20)
howManyQuestionsLab.grid(column=1, row=6)
howManyQuestionsEnt = Entry(app, bd=3)
howManyQuestionsEnt.grid(column=2, row=6)
howManyQuestionsBtn = Button(app, text="Submit", command=questionCount)
howManyQuestionsBtn.grid(column=3, row=6)

questionVal = Label(app, text="Max number to be asked to go to")
questionVal.grid(column=1, row=7, pady=20, padx=20)
questionEnt = Entry(app, bd=3)
questionEnt.grid(column=2, row=7)
questionSubmit = Button(app, text="Submit", bd=3, command=questionAns)
questionSubmit.grid(column=3, row=7)

genMath = Label(app, text="", padx=10, pady=10)
genMath.grid(column=1, row=8)

userQuesLabel = Label(app, text="Your Answer", padx=10, pady=10)
userQuesLabel.grid(column=1, row=9)
userAns = Entry(app, bd=3)
userAns.grid(column=2, row=9)
userSubmit = Button(app, bd=3, text="Submit", command=getUserAnswer)
userSubmit.grid(column=3, row=9)

ansResult = Label(app, text=" ", font=("Courier", 9))
ansResult.grid(column=1, row=10)

errorLabel = Label(app, text="")
errorLabel.grid(column=1, row=11)

app.mainloop()