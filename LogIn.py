import tkinter as tk
import tkinter.messagebox as tm
import loaders

TITLE_FONT = ("Helvetica", 18, "bold")

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
                            command=lambda : self.controller.show_frame("Register"))
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

