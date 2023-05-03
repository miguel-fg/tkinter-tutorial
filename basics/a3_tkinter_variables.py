import tkinter as tk
from tkinter import ttk


def button_func():
    print(string_var.get())
    string_var.set("button pressed")


# window
window = tk.Tk()
window.title("Tkinter Variables")
window.geometry("300x400")

# tkinter variable
string_var = tk.StringVar(value="start value")

"""
there's also:

IntVar
DoubleVar
BooleanVar
"""

# widgets
label = ttk.Label(master=window, textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

# any widgets that share the string variable will be affected
entry2 = ttk.Entry(master=window, textvariable=string_var)
entry2.pack()

button = ttk.Button(master=window, text="button", command=button_func)
button.pack()

# EXERCISE: Create 2 entry fields and 1 label, they should all be connected via a StringVar
# set a start value of "test"

exercise_var = tk.StringVar(value="test")

e_entry1 = ttk.Entry(master=window, textvariable=exercise_var)
e_entry1.pack()
e_entry2 = ttk.Entry(master=window, textvariable=exercise_var)
e_entry2.pack()

e_label = ttk.Label(master=window, textvariable=exercise_var)
e_label.pack()


# run
window.mainloop()
