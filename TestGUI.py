import tkinter as tk
import tkinter.messagebox as tm
import loaders
from tkinter import *
from Test import Test
import webbrowser
from LogIn import * 

TITLE_FONT = ("Helvetica", 18, "bold")

# Administrator account can be only created by software package programmer,
# therefore adding administrator acount is not allowed.
class TestGUI(tk.Frame):

    def __init__(self, parent, controller, test):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Make a scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Need to make a canvas with a frame inside it in order to scroll: see
        # here: http://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341#3092341
        canvas = tk.Canvas(self, yscrollcommand=scrollbar.set, width=800, height=600)
        canvas.pack(side=TOP, expand=True)
        scrollbar.configure(command=canvas.yview)
        frame = tk.Frame(canvas)
        canvas.create_window((1, 1), window=frame, anchor="nw", tags="frame")
        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox(ALL)))
        canvas.configure(scrollregion=canvas.bbox(ALL))

        self.correctLabels = []
        self.incorrectLabels = []

        # A list to hold the IntVars for multiple choice questions and Entrys for
        # open questions
        self.vars = []

        # Keep track of the submit buttons so we can remove them once clicked
        self.submit_buttons = []

        for idx, question in enumerate(test.getNextQuestion(), start=0): # usage of Test class generator (yielding)
            task = Label(frame, text = "Task " + (str(idx + 1) + ". " + question.getQuestionText()), font = ('MS', 10, 'bold'), justify=LEFT, wraplength=500)
            task.grid(row = idx * 10 + 1, column = 1, columnspan = 7)

            if question.isQuestionMultipleChoice():
                options = question.getOptions()
                radio  = [None] * 4
                answer = [None] * 4

                self.vars.append(IntVar())

                # Displaying answers
                for i in range(4):
                    radio[i] = Radiobutton(frame, variable=self.vars[-1], value=i+1)
                    radio[i].grid(row = idx * 10 + 2, column=i * 2 + 1, sticky=E)
                    answer[i] = Label(frame, text = options[i], font = ('MS', 10, 'bold'))
                    answer[i].grid(row = idx * 10 + 2, column=i * 2 + 2, sticky=W)

            else:
                entAns = Entry(frame)
                entAns.grid(row = idx * 10 + 2, column = 1, columnspan=4)
                self.vars.append(entAns)


            mark = Label(frame, text = '(' + str(question.getAvailableMarks()) + ' marks)', font = ('MS', 10, 'bold'))
            mark.grid(row = idx * 10 + 6, column = 8, sticky=E)

            butSubmit = Button(frame, text = 'Submit', font = ('MS', 10,'bold'))
            butSubmit['command'] = self.submit_command(question, idx, test)
            butSubmit.grid(row = idx * 10 + 7, column = 8, sticky=E)
            self.submit_buttons.append(butSubmit)

            # If it is a multiple choice q then answer is 1,2,3 or 4, NOT the
            # actual option
            if question.isQuestionMultipleChoice():
                correctAnswerIndex = int(question.getCorrectAnswer()) - 1
                answer = question.getOptions()[correctAnswerIndex]
            else:
                answer = question.getCorrectAnswer()

            correctLabel = Label(frame, text="Correct", font=('MS', 10, 'bold'))
            incorrectLabel = Label(frame, text="Incorrect. Correct answer was: " + answer, font = ('MS', 10, 'bold'))

            self.correctLabels.append(correctLabel)
            self.incorrectLabels.append(incorrectLabel)
            
        testSubmit = Button(frame, text = 'Submit Test', font = ('MS', 10, 'bold'))
        testSubmit['command'] = self.submitTest()
        testSubmit.grid(row = idx * 10 + 8, column = 4, sticky=E)
        
        


    def submit_command(self, question, idx, test):
        return lambda: self.evaluateAnswer(question, idx, test)

    def evaluateAnswer(self, question, idx, test):

        answer = str(self.vars[idx].get())
        print("You chose " + str(answer))

        print("Correct answer is " + question.getCorrectAnswer())

        if question.isAnswerCorrect(USER_ID, answer):
            self.correctLabels[idx].grid(row=idx * 10 + 3, column=1, sticky=W)
        else:
            self.incorrectLabels[idx].grid(row=idx * 10 + 3, column=1, sticky=W)

        self.submit_buttons[idx].grid_remove()
        test.addQuestionResult(USER_ID, question)
        
    def submitTest(self):
        pass
