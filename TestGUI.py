import tkinter as tk
import tkinter.messagebox as tm
import loaders
from tkinter import *
from Test import Test
import webbrowser
from LogIn import *
import csv

TITLE_FONT = ("Helvetica", 18, "bold")
FONT = ("MS", 10, "normal")
BOLD_FONT = ("MS", 10, "bold")

# Administrator account can be only created by software package programmer,
# therefore adding administrator acount is not allowed.
class TestGUI(tk.Frame):


    def __init__(self, parent, controller, test):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.test = test

        # Keep track of how many questions have been answered
        self.answered = 0

        # Make a scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Need to make a canvas with a frame inside it in order to scroll: see
        # here: http://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341#3092341
        canvas = tk.Canvas(self, yscrollcommand=scrollbar.set, width=1000, height=600)
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

        testTitle = Label(frame, text=test.getTestName(), font=TITLE_FONT, wraplength=750)
        testTitle.grid(row = 1, column = 1, columnspan = 7)

        introductionText = Label(frame, text=test.getIntroductionText(), font=FONT, wraplength=750,
                                 pady=20)
        introductionText.grid(row = 2, column = 1, columnspan = 7)

        for idx, question in enumerate(test.getNextQuestion(), start=0): # usage of Test class generator (yielding)
            task = Label(frame, text = "Task " + (str(idx + 1) + ". " + question.getQuestionText()), font = FONT, justify=LEFT, wraplength=500)
            task.grid(row = idx * 10 + 6, column = 0, columnspan = 7)

            if question.isQuestionMultipleChoice():
                options = question.getOptions()
                radio  = [None] * 4
                answer = [None] * 4

                self.vars.append(IntVar())

                # Displaying answers
                for i in range(4):
                    radio[i] = Radiobutton(frame, variable=self.vars[-1], value=i+1)
                    radio[i].grid(row = idx * 10 + 8, column=i + 2, sticky=E)
                    answer[i] = Label(frame, text = options[i], font = FONT)
                    answer[i].grid(row = idx * 10 + 8, column=i + 3, sticky=W)

            else:
                entAns = Entry(frame)
                entAns.grid(row = idx * 10 + 8, column = 1, columnspan=4)
                self.vars.append(entAns)


            mark = Label(frame, text = '(' + str(question.getAvailableMarks()) + ' marks)', font = FONT)
            mark.grid(row = idx * 10 + 8, column = 6, sticky=E)

            butSubmit = Button(frame, text = 'Submit', font = BOLD_FONT)
            butSubmit['command'] = self.submit_command(question, idx, test)
            butSubmit.grid(row = idx * 10 + 10, column = 6, sticky=E)
            self.submit_buttons.append(butSubmit)

            # If it is a multiple choice q then answer is 1,2,3 or 4, NOT the
            # actual option
            if question.isQuestionMultipleChoice():
                correctAnswerIndex = int(question.getCorrectAnswer()) - 1
                answer = question.getOptions()[correctAnswerIndex]
            else:
                answer = question.getCorrectAnswer()

            correctLabel = Label(frame, text="Correct", font=BOLD_FONT)
            incorrectLabel = Label(frame, text="Incorrect. Correct answer was: " + answer, font = BOLD_FONT)

            self.correctLabels.append(correctLabel)
            self.incorrectLabels.append(incorrectLabel)

        self.testSubmit = Button(frame, text = 'Submit Test', font = BOLD_FONT, command=lambda :  self.submitTest(test))
        #self.testSubmit['command'] = self.submitTest(test)
        self.testSubmit.grid(row = idx * 10 + 11, column = 4, sticky=E)
        # Hide submit button until all questions have been answered
        self.testSubmit.grid_forget()


    def submit_command(self, question, idx, test):
        return lambda: self.evaluateAnswer(question, idx, test)

    def evaluateAnswer(self, question, idx, test):

        USER_ID = self.controller.USER_ID
        answer = str(self.vars[idx].get())

        if question.isAnswerCorrect(USER_ID, answer):
            self.correctLabels[idx].grid(row=idx * 10 + 12, column=1, sticky=E)
        else:
            self.incorrectLabels[idx].grid(row=idx * 10 + 12, column=1, sticky=E)

        self.submit_buttons[idx].grid_remove()
        test.addQuestionResult(USER_ID, question)

        self.answered += 1
        if self.answered == test.getNumberOfQuestions():
            self.testSubmit.grid()

    def submitTest(self, test):
        USER_ID = self.controller.USER_ID
        result = test.getTestResult(USER_ID)

        with open('StoreResults.csv', 'a') as f:
            w = csv.DictWriter(f, ["studentID", "TestID", "Total"])
            testing = {}
            testing = {"studentID":USER_ID, "TestID":test.getTestID(), "Total": result}
            w.writerow(testing)

        tm.showinfo("Test Submission", "Test has been submited successfully! Your score was: {}/{}".format(result, test.getTotalAvailableMarks()))

        self.controller.show_frame("HomePage")
