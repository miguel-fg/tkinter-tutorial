import tkinter as tk
from tkinter import ttk

"""
IMPORTANT NOTES:
Tkinter lacks inbuilt tools for responsive layouts (i.e. layouts cannot be "updated").

A separate layout is needed for each window size.

The SizeNotifier class is reusable in case other projects need responsive layouts.
"""


class App(tk.Tk):
    def __init__(self, start_size):
        super().__init__()
        self.title("Responsive layout")
        self.geometry(f"{start_size[0]}x{start_size[1]}")

        # setting a starting empty frame
        self.frame = ttk.Frame(master=self)
        self.frame.pack(expand=True, fill="both")

        # setting minimum width value thresholds
        SizeNotifier(
            self,
            {
                300: self.create_small_layout,
                600: self.create_medium_layout,
                1200: self.create_large_layout,
            },
        )

        # run
        self.mainloop()

    def create_small_layout(self):
        self.frame.pack_forget()  # removing previous layout
        self.frame = ttk.Frame(master=self)
        ttk.Label(master=self.frame, text="Label 1", background="red").pack(
            expand=True, fill="both", padx=10, pady=5
        )
        ttk.Label(master=self.frame, text="Label 2", background="green").pack(
            expand=True, fill="both", padx=10, pady=5
        )
        ttk.Label(master=self.frame, text="Label 3", background="blue").pack(
            expand=True, fill="both", padx=10, pady=5
        )
        ttk.Label(master=self.frame, text="Label 4", background="yellow").pack(
            expand=True, fill="both", padx=10, pady=5
        )

        self.frame.pack(expand=True, fill="both")

    def create_medium_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(master=self)

        self.frame.columnconfigure((0, 1), weight=1, uniform="a")
        self.frame.rowconfigure((0, 1), weight=1, uniform="a")
        self.frame.pack(expand=True, fill="both")

        ttk.Label(master=self.frame, text="Label 1", background="red").grid(
            column=0, row=0, sticky="nsew"
        )
        ttk.Label(master=self.frame, text="Label 2", background="green").grid(
            column=1, row=0, sticky="nsew"
        )
        ttk.Label(master=self.frame, text="Label 3", background="blue").grid(
            column=0, row=1, sticky="nsew"
        )
        ttk.Label(master=self.frame, text="Label 4", background="yellow").grid(
            column=1, row=1, sticky="nsew"
        )

    def create_large_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(master=self)

        ttk.Label(master=self.frame, text="Label 1", background="red").pack(
            expand=True, fill="both", side="left", padx=10, pady=5
        )
        ttk.Label(master=self.frame, text="Label 2", background="green").pack(
            expand=True, fill="both", side="left", padx=10, pady=5
        )
        ttk.Label(master=self.frame, text="Label 3", background="blue").pack(
            expand=True, fill="both", side="left", padx=10, pady=5
        )
        ttk.Label(master=self.frame, text="Label 4", background="yellow").pack(
            expand=True, fill="both", side="left", padx=10, pady=5
        )
        self.frame.pack(expand=True, fill="both")

    # EXERCISE:
    # Create a third layout where the widgets are next to each other
    # Make it appear once the window is wider than 1200 pixels


class SizeNotifier:
    def __init__(self, window, size):
        self.window = window
        self.size = {
            key: value for key, value in sorted(size.items())
        }  # copying the sorted dictionary
        self.current_min_size = None
        self.window.bind("<Configure>", self.check_size)  # listening for window changes

        # safety minimum values
        self.window.update()
        min_height = self.window.winfo_height()
        min_width = list(self.size)[0]
        self.window.minsize(min_width, min_height)

    def check_size(self, event):
        if event.widget == self.window:  # only check for changes in window size
            window_width = event.width
            checked_size = None

            for min_size in self.size:  # check every minimum size threshold
                delta = window_width - min_size  # checks for smallest positive number

                if delta >= 0:  # <- positive number
                    checked_size = min_size  # assigns threshold value

            if checked_size != self.current_min_size:  # updates size changes
                self.current_min_size = checked_size
                self.size[self.current_min_size]()


App((400, 300))
