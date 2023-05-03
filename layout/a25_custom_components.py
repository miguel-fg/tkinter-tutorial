import tkinter as tk
from tkinter import ttk

"""
For simple components, it's best to use the functional approach (create a widget in a function and return it). For complex components, it's better to use a class based approach.
"""


class App(tk.Tk):
    def __init__(self, title: str, dimensions: tuple):
        # setup
        super().__init__()
        self.title(title)
        self.geometry(f"{dimensions[0]}x{dimensions[1]}")

        # widgets
        Segment(self, "label", "button", "test 1")
        Segment(self, "test", "click", "test 2")
        Segment(self, "hello", "test", "test 3")
        Segment(self, "bye", "launch", "test 4")
        Segment(self, "last one", "exit", "test 5")

        # run
        self.mainloop()


# class based custom component
class Segment(ttk.Frame):
    def __init__(self, parent, label_text: str, button_text: str, button_text2: str):
        super().__init__(master=parent)

        # grid layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")

        # grid widgets
        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky="nsew")
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky="nsew")
        self.third_column(button_text2).grid(row=0, column=2, sticky="nsew")

        # packing the frame in the window
        self.pack(expand=True, fill="both", padx=10, pady=10)

    # EXERCISE:
    # Create a smaller widget inside of the Segment class using a function
    # It should be a container that has an entry field and a button stacked on top of each other
    # The button text should be set via parameters
    # All of this should be in the third column of the Segment grid
    def third_column(self, button_text: str):
        frame = ttk.Frame(master=self)

        ttk.Entry(master=frame).pack(expand=True, fill="both")
        ttk.Button(master=frame, text=button_text).pack(expand=True, fill="both")

        return frame


App("Widgets and return", (400, 600))
