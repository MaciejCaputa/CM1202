import tkinter as tk
import tkinter.messagebox as tm
import loaders

TITLE_FONT = ("Helvetica", 18, "bold")

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Home Page")
        label = tk.Label(self, text="Home Page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Lessons",
                            command=lambda: controller.show_frame("Lessons"))
        
        button2 = tk.Button(self, text="View Results",
                            command=lambda: controller.show_frame("HomePage"))
        
        button1.pack()
        button2.pack()