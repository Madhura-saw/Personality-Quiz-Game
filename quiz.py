# importing libraries
import random
import tkinter
from tkinter import *
from tkinter import font
from tracemalloc import start
from turtle import back, width
from PIL import ImageTk, Image

# list of questions for quiz
questions = [
    "In uncertain times, I usually expect the best?",
    "It's easy for me to relax?",
    "If something can go wrong for me, it will?",
    "I'm always optimistic about my future?",
    "I enjoy my friends a lot?",
    "It's important for me to keep busy?",
    "I hardly ever expect things to go my way?",
    "I don't get upset too easily?",
    "I rarely count on good things happening to me?",
    "I expect more good things to happen to me than bad?",
]

# list of values of answer choices for the respective qustions
answerChoice = [
    ["0", "1",],
    ["0", "1",],
    ["0", "1",],
    ["0", "1",],
    ["0", "1",],
    ["0", "1",],
    ["0", "1",],
    ["0", "1",],
    ["0", "1",],
    ["0", "1",],
]

# Lis of correct answers for corresponding questions
answers = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0]

user_answer = []    # list that will store all the answers entered by the user

index = []    # list of index that generates random numbers for the questions that will be displayed

# this function will generate the random indexes and store them in the index list
def gen():
    global index
    while len(index) < 10:
        x = random.randint(0, 9)
        if x in index:
            continue
        else:
            index.append(x)

# this will destroy the 2nd screen that generates the questions and options, it takes the parameter score from the calc() function
def showResult(scr):
    lblQuestions.destroy()
    r1.destroy()
    r2.destroy()

    # the score is divided in 3 categories and the widgets are displayed accordingly
    def seeResult():
        # for score less than 4 ie 0-3
        if scr < 4:               
            res1 = tkinter.Label(
                window,                                   # tkinter window
                text="YOU ARE A HALF GLASS EMPTY PERSON", # text
                font=("Monaco", 30, "bold"),              # font and styling of the text
                justify="center",                         # this aligns the text in the center of the window
                background="#ffffff",                     # gives a white background to the text
                wraplength=400,                           # wraps the text in 400 pixels if exceeded moves the text to the next line
            )
            res1.pack(pady=20)      # padding around the y axis

        # for score between 4-7
        elif scr >= 4 and scr < 8:
            res2 = tkinter.Label(
                window,
                text="YOU ARE A PESSIMIST BUT YOU CAN CHANGE YOURSELF",
                font=("Monaco", 30, "bold"),
                justify="center",
                background="#ffffff",
                wraplength=400,
            )
            res2.pack(pady=20)
        
        # for score above 8
        elif scr >= 8:
            res3 = tkinter.Label(
                window,
                text="CONGRATS ! YOU ARE A HALF GLASS FULL PERSON",
                font=("Monaco", 30, "bold"),
                justify="center",
                background="#ffffff",
                wraplength=400,
            )
            res3.pack(pady=20)
    
    # text label at the top
    askLabel = tkinter.Label(
        window,
        text="WHICH ONE ARE YOU ?",
        font=("Monaco", 30, "bold"),
        justify="center",
        background="#ffffff",
    )
    askLabel.pack(pady=20)
    
    # image below the text label
    global showImg      # image is made global
    showImg = ImageTk.PhotoImage(Image.open("glass.jpeg"))   # image opened using the pil library functions
    showLabel = tkinter.Label(window, image=showImg)
    showLabel.pack(pady=20)    

    askLabel2 = tkinter.Label(
        window,
        text="LET'S SEE !",
        font=("Monaco", 30, "bold"),
        justify="center",
        background="#ffffff",
    )
    askLabel2.pack(pady=20)

    # button that will display the results when pressed
    resultBtn = tkinter.Button(
        window,
        text="RESULT",
        font=("Times", 25, "bold"),
        justify="center",
        background="#ffffff",
        border=0.0,
        relief=FLAT,          # flat button
        command=seeResult,    # seeresult function is called which displays the result
    )
    resultBtn.pack(pady=20)

# the user answers and correct answers are verified and score is calculated
def calc():
    global index, user_answer, answers
    x = 0
    score = 0
    for i in index:
        if user_answer[x] == answers[i]:
            score += 1
        x += 1
    print(score)
    showResult(score)     # showResult function is called where the calculated score is passed as the parameter


ques = 1              
def selected():
    global radiovar, user_answer
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = rbvar.get()      
    user_answer.append(x)    # user answers are added to the user_answer list
    rbvar.set(-1)            # it is again set to default

    # if 10 questions are done then calc() function is called
    if ques < 10:
        lblQuestions.config(text=questions[index[ques]])
        ques += 1
    else:
        print(index)
        print(user_answer)
        calc()

# This will build the new window that displays the quiz questions
def startQuiz():
    global lblQuestions, r1, r2
    lblQuestions = tkinter.Label(
        window,
        text=questions[index[ques]],     # the index of the question is changed as per the random numbers generated in the index list
        font=("Textile", 20),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestions.pack(pady=(100, 30))

    global rbvar 
    rbvar = IntVar()     # this checks the value that is returned when the user chooses an option
    rbvar.set(-1)

    # radio button for agree
    r1 = tkinter.Radiobutton(
        window,
        text="Agree",
        font=("Times", 18),
        value=0,
        variable=rbvar,           # variable is given which will return the value
        background="#ffffff",
        command=selected,         # selected() is called if the button is pressed
    )
    r1.pack()

    # radio button for disagree
    r2 = tkinter.Radiobutton(
        window,
        text="Disagree",
        font=("Times", 18),
        value=1,
        variable=rbvar,           # variable is given which will return the value
        background="#ffffff",
        command=selected,         # selected() is called if the button is pressed
    )
    r2.pack()


def startPressed(): 
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    text.destroy()
    btnStart.destroy()
    gen()
    startQuiz()


window = tkinter.Tk()
window.title("OPTIMIST/PESSIMIST QUIZ")
window.geometry("750x700")
window.config(background="#ffffff")

# Image at the top
img = Image.open("thumbs.png")
img = img.resize((350, 250), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img)
l1 = Label(image=img1)
l1.pack(pady=(40, 0))

# text below the image
text = tkinter.Label(
    window,
    text="TAKE THE QUIZ TO KNOW!",
    font=("Comic Sans MS", 25, "bold"),
    background="#ffffff",
)
text.pack()

# Button to start
img2 = Image.open("start.png")
img2 = img2.resize((100, 50), Image.ANTIALIAS)
btnimage = ImageTk.PhotoImage(img2)
btnStart = tkinter.Button(
    window, image=btnimage, border=0, relief=FLAT, command=startPressed
)
btnStart.pack(pady=(50, 20))

# Instruction label
l2 = tkinter.Label(
    window,
    text="Read the Instructions\nClick 'START' once you are ready!",
    background="#ffffff",
    font=("Consolas", 15),
    justify="center",
)
l2.pack()

# Instructions
l3 = tkinter.Label(
    window,
    text="1.This quiz contains 10 questions.\n2.Each question has 2 options either AGREE or DISAGREE.\n3.You can select only one option.\n4.All questions are compulsory.\n5.Score will be displayed at the end",
    background="#ffffff",
    font=("Consolas", 15),
    justify="center",
)
l3.pack(pady=20)

# ALL THE BEST TEXT
l4 = tkinter.Label(
    window,
    text="🔴 ALL THE BEST 🔴",
    background="#ffffff",
    font=("Monaco", 30, "bold"),
    justify="center",
)
l4.pack()

window.mainloop()
