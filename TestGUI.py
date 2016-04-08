import tkinter as tk
import tkinter.messagebox as tm
import loaders
from tkinter import *
from Test import Test

TITLE_FONT = ("Helvetica", 18, "bold")

# Administrator account can be only created by software package programmer,
# therefore adding administrator acount is not allowed.
class TestGUI(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.createTestQuestion(Test.getTest("1"))

    def evaluateAnswer(self):
            pass
    
    def createTestQuestion(self, test):
#         for q in test.getNextQuestion():
        print("test")
        i = 1
        for idx, question in enumerate(test.getNextQuestion(), start=0): # usage of Test class generator (yielding)
            task = Label(self, text = (str(idx + 1) + ". " + question.getQuestionText()), font = ('MS', 10, 'bold'))
            task.grid(row = idx * 10, column = 0, columnspan = 2)
            

            if (question.isQuestionMultipleChoice()):
                options = question.getOptions()
                radio  = [None] * 4
                answer = [None] * 4

                
                self.var = IntVar()

                # Displaying answers
                for i in range(4):
                    radio[i] = Radiobutton(self, variable = self.var, value = 1)
                    radio[i].grid(row = idx * 10 + 1 + i, column = 0)
                    answer[i] = Label(self, text = options[i], font = ('MS', 10, 'bold'))
                    answer[i].grid(row = idx * 10 + 1 + i, column = 1, sticky=W)

                mark = Label(self, text = '(' + str(question.getAvailableMarks()) + ' marks)', font = ('MS', 10, 'bold'))
                mark.grid(row = idx * 10 + 5, column = 3, columnspan = 1)
            
                butSubmit = Button(self, text = 'Submit', font = ('MS', 10,'bold'))
                butSubmit['command'] = self.evaluateAnswer
                butSubmit.grid(row = idx * 10 + 6, column = 3)
                
            else:       
                self.entAns = Entry(self)
                self.entAns.grid(row = idx * 8 + 1, column = 1, columnspan = 2, sticky = E)
            