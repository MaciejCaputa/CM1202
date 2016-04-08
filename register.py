import tkinter as tk
import tkinter.messagebox as tm
import loaders

TITLE_FONT = ("Helvetica", 18, "bold")

# Administrator account can be only created by software package programmer,
# therefore adding administrator acount is not allowed.
class Register(tk.Frame):
    
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

        self.entry = [None] * 6
        self.entry[0] = tk.Entry(self)
        self.entry[1] = tk.Entry(self)
        self.entry[2] = tk.Entry(self)
        self.entry[3] = tk.Entry(self, show="*")

        for i in range(4):
            self.label[i].grid(row=i+1, column=0)
            self.entry[i].grid(row=i+1, column=1)
        
        self.account_type = 0
        self.radiobutton = [None] * 3
        self.radiobutton[0] = tk.Radiobutton(self, text="Student", variable=self.account_type, value=0, command=self.student)

        self.radiobutton[1] = tk.Radiobutton(self, text="Lecturer", variable=self.account_type, value=1, command=self.lecturer)

        self.radiobutton[0].grid(row=5, column=1)
        self.radiobutton[1].grid(row=5, column=2)
        self.radiobutton_label = tk.Label(self, text="Account type")
        self.radiobutton_label.grid(row=5, column=0)

        self.button = tk.Button(self, text="Submit", command=self.register)
        self.button.grid(row=8, columnspan=2)

    def student(self):
        self.account_type = "Student"

        self.label[4] = tk.Label(self, text="Year   ")
        self.label[5] = tk.Label(self, text="Course ")
        self.label[4].grid(row=6,column=0)
        self.label[5].grid(row=7,column=0)

        self.entry[4] = tk.Entry(self)
        self.entry[5] = tk.Entry(self)
        self.entry[4].grid(row=6,column=1)
        self.entry[5].grid(row=7,column=1)

    def lecturer(self):
        self.account_type = "Lecturer"

        self.label[4] = tk.Label(self, text="School")
        self.label[5] = tk.Label(self, text="Modules")
        self.label[4].grid(row=6,column=0)
        self.label[5].grid(row=7,column=0)

        self.entry[4] = tk.Entry(self)
        self.entry[5] = tk.Entry(self)
        self.entry[4].grid(row=6,column=1)
        self.entry[5].grid(row=7,column=1)

    def register(self):
        print(self.entry)
        print(self.account_type)
        username    = self.entry[0].get()
        forename    = self.entry[1].get()
        surname     = self.entry[2].get()
        password    = self.entry[3].get()

        if not (username and forename and surname and password):
            # Checking if all fields are filled
            tm.showerror("Registration Failed!", "Pleas fill all required fields.")
            return

        if self.account_type == "Student":
            year        = self.entry[4].get()
            course      = self.entry[5].get()

            if not (year and course):
                # Checking if all fields are filled
                tm.showerror("Registration Failed!", "Pleas fill all required fields.")
                return

            if loaders.database["students"].addAccount(username, forename, surname, password, year, course):
                tm.showinfo("Account added successfuly", "Pleas log in into the system")
                self.controller.show_frame("LogIn")
            else:
                tm.showerror("Registration Failed!", "Account cannot be added. Username already exists.")

        if self.account_type == "Lecturer":
            school      = self.entry[4].get()
            modules     = self.entry[5].get()

            if not (school and modules):
                # Checking if all fields are filled
                tm.showerror("Registration Failed!", "Pleas fill all required fields.")
                return

            if loaders.database["lecturers"].addAccount(username, forename, surname, password, school, modules):
                tm.showinfo("Account added successfuly", "Pleas log in into the system")
                self.controller.show_frame("LogIn")
            else:
                tm.showerror("Registration Failed!", "Account cannot be added. Username already exists.")







