import tkinter as tk
import tkinter.messagebox as tm
import loaders
from register import * 

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
        for F in (LogIn, RegisterStudent, HomePage, ViewLessons, TakeTests):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

            #frame.pack(expand=True)

        self.show_frame("LogIn")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


class LogIn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.controller.title("Log In")

        self.label = tk.Label(self, text="Log In", font=TITLE_FONT)
        self.label.grid(columnspan=2)


        self.label1 = tk.Label(self, text="Username")
        self.label2 = tk.Label(self, text="Password")

        self.entry1 = tk.Entry(self)
        self.entry2 = tk.Entry(self, show="*")

        self.label1.grid(row=1, column=0)
        self.label2.grid(row=2, column=0)
        self.entry1.grid(row=1, column=1)
        self.entry2.grid(row=2, column=1)

        self.button1 = tk.Button(self, text="Login",
                            command=self.log_in)
        self.button1.grid(columnspan=2)

        self.button2 = tk.Button(self, text="Create new student account",
                            command=lambda : self.controller.show_frame("RegisterStudent"))
        self.button2.grid(columnspan=2)


        self.pack()

    def register(self):
        self.controller.show_frame("Register")

    def log_in(self):
        #print("Clicked")
        username = self.entry1.get()
        password = self.entry2.get()

        print(username, password)

        if loaders.database["students"].logIn(username, password):
            tm.showinfo("Login info", "Welcome " + username)

            self.controller.show_frame("HomePage")

        else:
            tm.showerror("Login error", "Incorrect username or password")


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Home Page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="View Lessons",
                            command=lambda: controller.show_frame("ViewLessons"))
        button2 = tk.Button(self, text="Take Tests",
                            command=lambda: controller.show_frame("TakeTests"))
        button1.pack()
        button2.pack()


class ViewLessons(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="View Lessons", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the home page",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()


class TakeTests(tk.Frame):

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