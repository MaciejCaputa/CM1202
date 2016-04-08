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
        
        q = next(test.getNextQuestion())
        
        lblStrQ1 = Label(self, text = (q.getQuestionText()), font = ('MS', 10, 'bold'))
        lblStrQ1.grid(row = 2, column = 1, columnspan = 5)
    
        if (q.isQuestionMultipleChoice()):
            options = q.getOptions()
            
            lblStrA1 = Label(self, text = options[0], font = ('MS', 10, 'bold'))
            lblStrA1.grid(row = 4, column = 1, columnspan = 1)
            
            lblStrA2 = Label(self, text = options[1], font = ('MS', 10, 'bold'))
            lblStrA2.grid(row = 5, column = 1, columnspan = 1)
            
            lblStrA3 = Label(self, text = options[2], font = ('MS', 10, 'bold'))
            lblStrA3.grid(row = 6, column = 1, columnspan = 1)
            
            lblStrA4 = Label(self, text = options[3], font = ('MS', 10, 'bold'))
            lblStrA4.grid(row = 7, column = 1, columnspan = 1)
            
            
            lblStrM1 = Label(self, text = '(' + str(q.getAvailableMarks()) + ' marks)', font = ('MS', 10, 'bold'))
            lblStrM1.grid(row = 8, column = 6, columnspan = 1)
            
            butSubmit = Button(self, text = 'Submit', font = ('MS', 10,'bold'))
            butSubmit['command'] = self.evaluateAnswer
            butSubmit.grid(row = 10, column = 6, columnspan = 1)
            
            self.varQ1 = IntVar()
            
            R1Q1 = Radiobutton(self, variable = self.varQ1, value = 1)
            R1Q1.grid(row = 4, column = 2)
            
            R2Q1 = Radiobutton(self, variable = self.varQ1, value = 2)
            R2Q1.grid(row = 5, column = 2)
            
            R3Q1 = Radiobutton(self, variable = self.varQ1, value = 3)
            R3Q1.grid(row = 6, column = 2)
            
            R4Q1 = Radiobutton(self, variable = self.varQ1, value = 4)
            R4Q1.grid(row = 7, column = 2)
            
        else:       
            self.entAns = Entry(self)
            self.entAns.grid(row = 4, column = 3, columnspan = 2, sticky = E)
        