import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Layout Intro")
window.geometry("600x400")

# widgets
label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue")

# pack

"""
label1.pack(
    side="left", expand=True, fill="both"
)  # expand=True means the widget will use all the available space, fill will adjust the size of the widget to all the available space in "x", "y", or "both"
label2.pack(side="left", expand=True, fill="both")
"""
# grid
"""
# defining 3 columns, the third one being twice as wide
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=2)

# defining rows
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

# assigning a widget to a grid position
label1.grid(row=0, column=1, sticky="nsew")  # sticky uses compass directions
label2.grid(row=1, column=1, columnspan=2, sticky="nsew")
"""

# place
label1.place(
    x=100, y=200, width=200, height=100
)  # the coordinates correspond to the top left of all widgets
label2.place(
    relx=0.5, rely=0.5, relwidth=1, anchor="center"
)  # translates the size of the window to values between 0 and 1
# anchor is the point of the widget that is placed, it uses compass directions (except center)

# run
window.mainloop()
