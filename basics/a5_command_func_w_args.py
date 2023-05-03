import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("buttons, functions and arguments")

# widgets
entry_str = tk.StringVar(value="test")
entry = ttk.Entry(master=window, textvariable=entry_str)
entry.pack()

def button_func(entry_string):
    print("a button was pressed")
    print(entry_string.get())

#the easiest way to make a button call a function with arguments is wrapping it inside a lambda function
button = ttk.Button(master=window, text="button", command= lambda: button_func(entry_str))
button.pack()

"""
OPTION 2:
Make 2 functions wrapped around each other:

    outer_func(parameter):
        def inner_func():
            print("a button was pressed)
            print(parameter.get())

        return inner_func

    button = ttk.Button(master=window, text="button", command = outer_func(parameter))

Both solutions are equivalent.
"""

window.mainloop()
