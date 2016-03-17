from tkinter import *
import tkinter.messagebox as tm
import loaders


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Username")
        self.label_2 = Label(self, text="Password")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clickked(self):
        #print("Clicked")
        username = self.entry_1.get()
        password = self.entry_2.get()

        print(username, password)

        if loaders.database["students"].logIn(username, password):
            tm.showinfo("Login info", "Welcome " + username)
            lf.quit()
            hf = HomeFrame(root)
        else:
            tm.showerror("Login error", "Incorrect username or password")


class HomeFrame(Frame):
    def __init__(self, master):
        super().__init__(master)


        self.button_1 = Button(self, text="View Lessons", command = self.view_lessons)
        self.button_2 = Button(self, text="Take Tests", command = self.take_tests)
        self.button_3 = Button(self, text="See Results", command = self.see_results)

        self.button_1.grid(row=0, sticky=E)
        self.button_2.grid(row=1, sticky=E)
        self.button_3.grid(row=2, column=1)

        self.pack()

    def view_lessons(self):
    	pass

    def take_tests(self):
    	pass

    def see_results(self):
    	pass



root = Tk()
root.geometry("800x600")
root.title("Log In")
root.configure(background="grey")

lf = LoginFrame(root)
lf.pack(expand=1)  # same as expand=True

root.mainloop()