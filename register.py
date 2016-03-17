import tkinter as tk
import tkinter.messagebox as tm
import loaders

TITLE_FONT = ("Helvetica", 18, "bold")

class RegisterStudent(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Register")
        self.title = tk.Label(self, text="Register", font=TITLE_FONT)
        self.title.grid(columnspan=2)

        self.label = [None] * 6
        self.label[0] = tk.Label(self, text="Username")
        self.label[1] = tk.Label(self, text="Forename")
        self.label[2] = tk.Label(self, text="Surname")
        self.label[3] = tk.Label(self, text="Password")
        self.label[4] = tk.Label(self, text="Year")
        self.label[5] = tk.Label(self, text="Course")

        self.entry = [None] * 6
        self.entry[0] = tk.Entry(self)
        self.entry[1] = tk.Entry(self)
        self.entry[2] = tk.Entry(self)
        self.entry[3] = tk.Entry(self, show="*")
        self.entry[4] = tk.Entry(self)
        self.entry[5] = tk.Entry(self)

        for i in range(6):
            self.label[i].grid(row=i+1, column=0)
            self.entry[i].grid(row=i+1, column=1)

        self.button = tk.Button(self, text="Submit", command=self.register)
        self.button.grid(columnspan=2)

    def register(self):
        print(self.entry)
        username    = self.entry[0].get()
        forename    = self.entry[1].get()
        surname     = self.entry[2].get()
        password    = self.entry[3].get()
        year        = self.entry[4].get()
        course      = self.entry[5].get()

        if loaders.database["students"].addAccount(username, forename, surname, password, year, course):
            tm.showinfo("Account added successfuly", "Pleas log in into the system")
            self.controller.show_frame("LogIn")
        else:
            tm.showinfo("Warning!", "Account cannot be added. Username already exists.")







