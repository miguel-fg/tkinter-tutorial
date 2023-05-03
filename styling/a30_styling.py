import tkinter as tk
from tkinter import ttk, font

"""
Tkinter has a few styling options
    1. Inbuilt styling tools (widget options and the style object)
    2. External themes
    3. External modules (customtkinter and ttkbootstrap)

    First two options are terrible, and it's best to focus on external modules
"""


class App(tk.Tk):
    def __init__(self, size):
        super().__init__()

        # setup
        self.title("Styling")
        self.geometry(f"{size[0]}x{size[1]}")

        # use print(font.families()) to see a list of available fonts

        # widgets
        self.label = ttk.Label(
            master=self,
            text="A label\nAnd then type on another line",
            background="red",
            foreground="white",  # white text
            font=("Jokerman", 20),
            justify="right",
        )
        self.label.pack()

        # buttons don't share the same styling options, one of the reasons it is not a good styling practice

        # style object
        self.style = ttk.Style()
        # use print(style.theme_names()) to see available themes (all are incredibly old)
        # style.theme_use("clam")

        self.style.configure(
            "new.TButton", foreground="green", font=("Jokerman", 20)
        )  # uses T + name of widget to change all widgets in that category OR use new. to only affect desired widgets

        self.style.map(
            "new.TButton",
            foreground=[("pressed", "red"), ("disabled", "yellow")],
            background=[("pressed", "green"), ("active", "blue")],
        )

        self.button = ttk.Button(master=self, text="A button", style="new.TButton")
        self.button.pack()

        # EXERCISE
        # Add a frame with a width and height, give it a pink background color

        self.style.configure("new.TFrame", background="pink")

        self.frame = ttk.Frame(master=self, height=80, width=200, style="new.TFrame")
        self.frame.pack()

        # run
        self.mainloop()


App((400, 300))
