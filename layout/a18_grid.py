import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry("600x400")
window.title("Tkinter Grid")

# widgets
label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue")
label3 = ttk.Label(master=window, text="Label 3", background="green")
label4 = ttk.Label(master=window, text="Label 4", background="yellow")

button1 = ttk.Button(master=window, text="Button 1")
button2 = ttk.Button(master=window, text="Button 2")

entry = ttk.Entry(master=window)

# define a grid

# the uniform argument in column and row configure can be used to ensure equal sized rows and columns, use the same string argument for every configure call
window.columnconfigure(
    (0, 1, 2), weight=1, uniform="a"
)  # (index, weight), a tuple in the index indicates 3 columns with the same weight
window.columnconfigure(3, weight=2, uniform="a")

window.rowconfigure((0, 1, 2), weight=1, uniform="a")
window.rowconfigure(3, weight=3, uniform="a")

# place the widgets
label1.grid(row=0, column=0, sticky="nsew")  # (row, column)
label2.grid(row=1, column=1, rowspan=3, sticky="nsew")
label3.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)
label4.grid(row=3, column=3, sticky="se")

# EXERCISE
# Add the buttons and the entry field as the picture

button1.grid(row=0, column=3, sticky="nsew")
button2.grid(row=2, column=2, sticky="nsew")
entry.grid(row=2, column=3, rowspan=2)

# run
window.mainloop()
