import tkinter as tk
import tkinter.messagebox as tm
import loaders

from LogIn import *
from Register import *
from HomePage import *
from TestGUI import *

TITLE_FONT = ("Helvetica", 18, "bold")

class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", expand=True)
        #container.pack(side="top", fill="both", expand=True)
        container.configure(background="grey")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LogIn, Register, HomePage, Lessons, ViewLesson, TakeTest, TestGUI):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LogIn")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


class Lessons(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Lessons", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Probability",
                            command=lambda: controller.show_frame("ViewLesson"))
        
        button2 = tk.Button(self, text="Counting",
                            command=lambda: controller.show_frame("ViewLesson"))

        button3 = tk.Button(self, text="Go to the home page",
                            command=lambda: controller.show_frame("HomePage"))

        
        button1.pack()
        button2.pack()
        button3.pack()



class ViewLesson(tk.Frame):

    def __init__(self, parent, controller):      
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # constant id just for testing purposes, it will go into __init__
        lesson = loaders.database["lessons"].get_lesson(1)
        self.controller.title(lesson.topic + "(" + lesson.module + ")")
        self.title = tk.Label(self, text=lesson.topic + "(" + lesson.module + ")", font=TITLE_FONT)
        self.title.grid(columnspan=2)

        
        

        self.label = [None] * 6
        self.label[0] = tk.Label(self, text="test")
        self.label[1] = tk.Label(self, text=loaders.database["lessons"].get_lesson(1).content.introduction)


        for i in range(2):
            self.label[i].grid(row=i+1, column=0)
        

        button1 = tk.Button(self, text="Go to the lessons",
                           command=lambda: controller.show_frame("HomePage"))

        button2 = tk.Button(self, text="Take Test",
                   command=lambda: controller.show_frame("TestGUI"))

        button1.grid(row=8, columnspan=2)
        button2.grid(row=9, columnspan=2)


class TakeTest(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Take Tests", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the home page",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()


if __name__ == "__main__":
    app = GUI()
    app.geometry("800x600")

    app.mainloop()