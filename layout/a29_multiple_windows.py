import tkinter as tk
from tkinter import ttk, messagebox

"""
IMPORTANT NOTES:

Two options for extra windows:

    1. messagebox
        Specialised windows (alerts, yes/no dialogs)
    2. tk.Toplevel
        Completely new window (can hold completely different layouts)
"""


class App(tk.Tk):
    def __init__(self, size: tuple):
        super().__init__()

        # setup
        self.title("Multiple windows")
        self.geometry(f"{size[0]}x{size[1]}")

        # widgets
        self.button1 = ttk.Button(
            master=self, text="open main window", command=self.create_window
        )
        self.button1.pack(expand=True)

        self.button2 = ttk.Button(
            master=self, text="close main window", command=self.close_window
        )
        self.button2.pack(expand=True)

        self.button3 = ttk.Button(
            master=self, text="create yes no window", command=self.ask_yes_no
        )
        self.button3.pack(expand=True)

        # run
        self.mainloop()

    # https://docs.python.org/3/library/tkinter.messagebox.html

    def ask_yes_no(self):
        # answer = messagebox.askquestion("Title", "body")

        # messagebox.showinfo("Info title", "Here is some info")
        messagebox.showerror("Info title", "Here is some info")

    def create_window(self):
        self.window = Window("extra window", (300, 400))

    def close_window(self):
        self.window.destroy()


class Window(tk.Toplevel):
    def __init__(self, title: str, size: tuple):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        ttk.Label(master=self, text="A label").pack()
        ttk.Button(master=self, text="A button").pack()
        ttk.Label(master=self, text="Another label").pack(expand=True)


App((600, 400))
