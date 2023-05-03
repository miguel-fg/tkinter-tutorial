import tkinter as tk
from tkinter import ttk
from random import randint, choice

"""
This example covers a Canvas object. But the exact same principle can be applied to Text and Treeview objects, which are also scrollable.

The only difference is that the Canvas object is the only one that needs the mousewheel event binding, as the others already behave like that
"""


class App(tk.Tk):
    def __init__(self, size: tuple):
        super().__init__()
        self.title("Scrolling")
        self.geometry(f"{size[0]}x{size[1]}")

        # canvas
        self.canvas = RandomCanvas(
            self, "white", (0, 0, 2000, 5000)
        )  # left, top, right, bottom

        # scrollbar

        # always use .place() with the scrollbar to put it on the right side
        # yview and yscrollcommand are needed to connect the scrollbar and canvas

        # the yview method lets the scrollbar control the canvas
        # the yscrollcommand parameter lets the canvas update the position of the scrollbar
        self.scrollbar = ttk.Scrollbar(
            master=self, orient="vertical", command=self.canvas.yview
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")

        # mousewheel scrolling
        self.canvas.bind(
            "<MouseWheel>", lambda e: self.canvas.yview_scroll(-e.delta // 60, "units")
        )

        # EXERCISE:
        # Create a horizontal scrollbar at the bottom and use it to scroll the canvas left and right
        # Add an event to scroll left / right on Ctrl + mousewheel
        self.horizontal_scroll(self.canvas).place(
            relx=0, rely=1, relwidth=1, anchor="sw"
        )

        # second mousewheel scrolling
        self.canvas.bind(
            "<Control-MouseWheel>",
            lambda e: self.canvas.xview_scroll(e.delta // 60, "units"),
        )

        self.mainloop()

    # experimenting with custom components
    def horizontal_scroll(self, canvas: tk.Canvas):
        scroll = ttk.Scrollbar(master=self, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=scroll.set)

        return scroll


# creating random figures in the canvas to visualize it
class RandomCanvas(tk.Canvas):
    def __init__(self, parent, bg_color: str, scroll: tuple):
        super().__init__(master=parent, bg=bg_color, scrollregion=scroll)

        self.create_line(0, 0, 2000, 5000, fill="green", width=10)

        for i in range(100):
            l = randint(0, 2000)
            r = l + randint(10, 500)
            t = randint(0, 5000)
            b = t + randint(10, 500)
            color = choice(("red", "green", "blue", "yellow", "orange"))

            self.create_rectangle(l, t, r, b, fill=color)

        self.pack(expand=True, fill="both")


App((600, 400))
