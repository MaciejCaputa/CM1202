import tkinter as tk
import tkinter.messagebox as tm
import loaders
import webbrowser

from LogIn import *
from register import *
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

        # Make frames for GUI
        for F in (LogIn, Register, HomePage, LecturerHomePage, Lessons, TakeTest, TestGUI):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        # Make frames for each lesson
        for lesson in loaders.database["lessons"].array:
            frame = ViewLesson(container, self, lesson)
            self.frames[lesson.topic] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        # Display log-in
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

        # Create buttons for each lesson
        for lesson in loaders.database["lessons"].array:
            button = tk.Button(self, text=lesson.topic,
                               command=self.button_command(lesson))
            button.pack()

        # A button to return to the home page
        home_button = tk.Button(self, text="Home",
                                command=lambda: controller.show_frame("HomePage"))
        home_button.pack()

    def button_command(self, lesson):
        return lambda: self.controller.show_frame(lesson.topic)


class ViewLesson(tk.Frame):

    def __init__(self, parent, controller, lesson):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        PARAGRAPH_PADDING = 7
        WRAP_LENGTH = 400

        # Make a scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Need to make a canvas with a frame inside it in order to scroll: see
        # here: http://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341#3092341
        canvas = tk.Canvas(self, yscrollcommand=scrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.configure(command=canvas.yview)
        frame = tk.Frame(canvas, height=1000)
        canvas.create_window((4, 4), window=frame, anchor="nw", tags="frame")
        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox(ALL)))
        canvas.configure(scrollregion=canvas.bbox(ALL))

        # Show the title
        title = "{} ({})".format(lesson.topic, lesson.module)
        self.controller.title(title)
        self.title = tk.Label(frame, text=title, font=TITLE_FONT)
        self.title.grid(columnspan=2)

        current_row = 1

        # Introduction
        intro_label = tk.Label(frame, text=lesson.content.introduction.strip(),
                               wraplength=WRAP_LENGTH)
        intro_label.grid(row=current_row, column=0, pady=PARAGRAPH_PADDING)
        current_row += 1

        # Paragraphs
        for (i, paragraph) in enumerate(lesson.content.paragraphs):
            label = tk.Label(frame, text=paragraph.body.strip(), wraplength=WRAP_LENGTH)
            label.grid(row=current_row, column=0, pady=PARAGRAPH_PADDING)
            current_row += 1

            # Show the image if there is one
            if paragraph.image is not None:
                photo = PhotoImage(file=paragraph.image)
                image_label = tk.Label(frame, text="picture", image=photo)

                # Need to keep a reference to the image, otherwise it appears
                # blank...
                image_label.image = photo

                image_label.grid(row=current_row, column=0, pady=PARAGRAPH_PADDING)
                current_row += 1

            # Show link if there is one
            if paragraph.link is not None:
                link_label = tk.Label(frame, text=paragraph.link, foreground="blue")

                # Open the link in a web browser when clicked
                link_label.bind("<Button-1>", lambda e: webbrowser.open(paragraph.link))

                # Set the cursor to make it more clear that this can be clicked
                link_label.config(cursor="hand2")

                link_label.grid(row=current_row, column=0, pady=PARAGRAPH_PADDING)
                current_row += 1

        # Summary
        summary = tk.Label(frame, text=lesson.content.summary, pady=PARAGRAPH_PADDING)
        summary.grid(row=current_row, column=0)
        current_row += 1

        button1 = tk.Button(frame, text="Go to the lessons",
                           command=lambda: controller.show_frame("Lessons"))

        button2 = tk.Button(frame, text="Take Test",
                   command=lambda: controller.show_frame("TestGUI"))

        button1.grid(row=current_row, columnspan=2)
        current_row += 1
        button2.grid(row=current_row, columnspan=2)


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